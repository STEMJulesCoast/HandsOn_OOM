# Objektorientierte Modellierung und Implementierung

Dieses Repository dient als Einführung in objektorientierte Modellelierung (OOM) und Programmierung (OOP). Enthalten sind die beiden UML-Klassendiagramme aus der [Storymap](https://storymaps.arcgis.com/stories/dd9d06f89a63400c96927de117a5b28a) als .uxf-files sowie ein Notebook mit dem Streamingdiesnt Beispiel. 
Hier wird eine Klasse mit spezifischen Attributen und Methoden definiert und eine Subklasse deklariert, die um zusätzliche Methoden erweitert wird. Dies veranschaulicht die Kernprinzipien der OOM (Abstraktion, Kapselung, Vererbung, Polymorphie) an einem OOP Beispiel. Als Übung kann das Programm um eine weitere Subklasse mit neuen Funktionen und Attributen erweitert werden.

Ein weiteres Beispiel umfasst die objektorientierte Modellierung in den Klimawissenschaften. In diesem Teil wird eine Klasse definiert, die es ermöglicht, den Langzeittrend aus Klimadaten zu dentfernen, Anomalien zu berechnen, Ergebnisse zu speichern und weitere Analysen durchzuführen. Diese Anwendungen zeigen, wie vielseitig objektorientierte Ansätze zur Lösung verschiedener Probleme eingesetzt werden können.

## Inhalt

- `example_exercise_OOP_Streaming.ipynb`: Ein einführendes Notebook, das die Grundlagen des OOP anhand eines Streamingdienstes erklärt. Enthält Übungsaufgaben.
- `example_exercise_OOP_Climate.ipynb`: Beispiel für OOP bei der Analyse von Klimadaten. Hier kann mit weiteren Datensätzen experimentiert werden und die Klasse um zusätzliche Methoden wie z.B. Berechnung von Mittelwerten erweitert werden.  
- `climate_data_processor.py`: enthält die zentrale Klasse für die Klimadatenanalyse  
- `OOM_diagram_Streaming.uxf` UML- Klassendiagramm bearbeitbar mit der UMLet Extension in VS Code oder online [hier](https://www.umletino.com/umletino.html)  
- `Beispiel_Film.mp4`: Ein kurzes Video, das von [Pexels](https://www.pexels.com) stammt und zur Demonstration der Video-Abspielfunktion genutzt wird.
- `Beispiel_Musik.mp3`: Ein kurzes Musikstück von [AudioFire](https://www.audiofire.com), das zur Demonstration der Audio-Abspielfunktion verwendet wird.


## Starten

Um mit den Notebooks zu arbeiten, müssen folgende Schritte durchgeführt werden:


1. Falls nicht vorhanden: [Python](https://www.python.org/downloads/) und [Jupyter](https://jupyter.org/install) installieren oder [VS Code](https://github.com/STEMJulesCoast/CO2_Emissions/blob/5b73a4c37699245143b63fa18969e78a799a6a94/README.md)  einrichten
2. Das Repository klonen oder als ZIP-Datei herunterladen und entpacken.
3. Die erforderlichen Abhängigkeiten über Pip installieren::
   ```bash
   pip install -r requirements.txt
   ```
4. Mit den Notebooks arbeiten

# Interaktive Umgebung ohne Installation

Um direkt in einem interaktiven Umfeld zu experimentieren, kann das Repository in Binder gestartet werden:

## Beispiel- und Übungsskript Social Media Account  

Momentan nicht via Binder verfügbar. 

## Beispiel- und Übungsskript Klimadaten-Prozessierung 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/STEMJulesCoast/HandsOn_OOM/main?labpath=example_exercise_OOP_Climate.ipynb)

## Zielgruppe

Dieses Repository richtet sich an Anfänger:innen, die praktische Erfahrungen sammeln und ihr Wissen vertiefen möchten. Es ist so gestaltet, dass Nutzer:innen ohne tiefe Programmierkenntnisse die Inhalte nachvollziehen und erweitern können.


## Beispielansätze und Beitrag

Beispielansätze zu den Übungen können auf [Anfrage](mailto:koehler@nat.hamburg) zugesendet werden. Feedback und Beiträge zu diesem Projekt sind jederzeit willkommen.
