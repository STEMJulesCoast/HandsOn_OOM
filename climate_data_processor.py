import xarray as xr
from scipy.signal import detrend
import matplotlib.pyplot as plt
import numpy as np

class ClimateDataProcessor:
    def __init__(self, dataset):
        self.dataset = dataset
        self.ds_anom_detrended = xr.Dataset()

    def compute_anomalies_and_detrend(self):
        for var in self.dataset.data_vars:
            # Check if variable has 'lat', 'lon', and 'time' dimensions
            if set(['lat', 'lon', 'time']).issubset(set(self.dataset[var].dims)):
                # Calculate the monthly climatology for each variable
                climatology = self.dataset[var].groupby('time.month').mean('time')

                # Calculate anomalies
                anomalies = self.dataset[var].groupby('time.month') - climatology

                # Detrend the anomalies
                detrended_anomalies = xr.apply_ufunc(
                    detrend,
                    anomalies.fillna(0),  # Fill NaNs with zeros for detrending
                    input_core_dims=[['time']],
                    output_core_dims=[['time']],
                    dask='allowed'
                ).where(~anomalies.isnull())  # Re-apply the NaN mask

                # Assign to the dataset and transpose dimensions
                self.ds_anom_detrended[var] = detrended_anomalies.transpose('time', 'lat', 'lon')

                # Copy attributes and update long_name
                self.ds_anom_detrended[var].attrs = self.dataset[var].attrs
                self.ds_anom_detrended[var].attrs['long_name'] = 'Detrended anomaly of ' + self.ds_anom_detrended[var].attrs['long_name']

        self.ds_anom_detrended.attrs['description'] = 'Contains detrended anomalies of all variables'

    def save_results(self, filepath):
        self.ds_anom_detrended.to_netcdf(filepath)

    
    def filter_and_analyze_cycle(self, variable, vmin = 0, vmax = 2, window_size = 15, background='white',):
        # Data Preparation
        clean_data = self.ds_anom_detrended[variable].dropna(dim='time', how='all')

        # Low-Pass Filter to remove high frequency variations
        low_pass = clean_data.rolling(time=window_size, center=True).mean()

        # difference of anomalies and low_pass to get higher frequency variations

        high_pass = clean_data - low_pass

        # Plotting Setup
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), facecolor=background)
        fig.subplots_adjust(hspace=0.5, wspace=0.5)

        # Apply background settings
        if background == 'black':
            for ax_row in axes:
                for ax in ax_row:
                    ax.set_facecolor('black')
                    ax.tick_params(axis='x', colors='white')
                    ax.tick_params(axis='y', colors='white')
                    ax.yaxis.label.set_color('white')
                    ax.xaxis.label.set_color('white')
                    ax.title.set_color('white')
                    ax.spines['bottom'].set_color('white')  # Set spine color
                    ax.spines['top'].set_color('white')     # Set spine color
                    ax.spines['right'].set_color('white')   # Set spine color
                    ax.spines['left'].set_color('white')    # Set spine color
        else:
            pass

        # Set color map
        cmap = 'plasma'

        # Plotting Data
        plots = [clean_data, low_pass, high_pass]
        titles = ['Original', 'Low-Pass', 'High-Pass']
        plot_axes = [axes[0, 0], axes[0, 1], axes[1, 1]] 
        for ax, data, title in zip(axes.flatten(), plots, titles):
            c=data.std(dim='time', ddof=1).plot(ax=ax, cmap=cmap,vmin=vmin, vmax=vmax)
            ax.set_title(title)
            if background == 'black':
                c.colorbar.set_label('Standard Deviation', color='white')  # Set colorbar label color
                c.colorbar.ax.yaxis.set_tick_params(color='white')  # Set colorbar ticks color
                plt.setp(plt.getp(c.colorbar.ax.axes, 'yticklabels'), color='white')
        axes[1, 1].axis('off')
        plt.show()

    def compute_fft(self, variable, lon_min, lon_max, lat_min, lat_max,time_start = None, time_end = None):
        
        # select time span, if necessary
        if time_start is not None:
            ds_sliced = self.ds_anom_detrended.sel(time=slice(time_start, time_end))  
        else:
            ds_sliced = self.ds_anom_detrended    
            
                                 
        # Adjust longitude boundaries if needed:
        # This code checks if the maximum longitude in the dataset exceeds 180 degrees,
        # indicating that the dataset uses a 0-360 degree format instead of the -180 to 180 degree format.
        # If true, it shifts both the minimum and maximum longitude values by 360 degrees to standardize the range.

        if ds_sliced.lon.max() > 181:
            lon_min = lon_min+360
            lon_max = lon_max+360

        # Compute the average value of the specified variable within the defined 
        # geographic box (longitude and latitude range).
        box_mean = ds_sliced[variable].sel(
            lon=slice(lon_min, lon_max), lat=slice(lat_min, lat_max)).mean(dim=['lon', 'lat'])
        
        # Perform a Fast Fourier Transform (FFT) on the averaged data to analyze its frequency components.
        fft_ds = np.fft.fft(box_mean)
        # Compute frequencies and corresponding periods for monthly data
        n = len(box_mean)
        freq = np.fft.fftfreq(n, d=1)  # d=1 assumes monthly data points
        # Periods will be in months
        periods = np.where(freq != 0, 1 / freq, np.inf)
        # Compute the Power Spectrum (amplitude squared)
        power_spec = np.abs(fft_ds)**2
        # Calculate a simple significance threshold, here set at mean + 2 * standard deviation
        threshold = np.mean(power_spec) + 2*np.std(power_spec)
        valid_periods = periods[:n // 2] > 0  # Exclude the infinite period at zero frequency

        significant_indices = np.where(power_spec[:n // 2][valid_periods] > threshold)[0]
        # Extract the corresponding significant periods
        significant_periods = periods[:n // 2][valid_periods][significant_indices]
        # Filter out infinite values from significant_periods
        significant_periods = significant_periods[np.isfinite(significant_periods)]
        # Print the significant periods
        print("Significant Periods (months)" , variable,":", significant_periods)
        