# WFY_Projekt 2025 : Einfaches Antivirus Projekt mit Flask

Dies Projekt ist ein kleines Antivirus-Programm was benutzen Python Flask und ein Machine Learning Modell. Es kann Dateien hochladen und überprüfen, ob da möglich ein Virus drinne ist.

## 🧠 Was macht das Projekt?

- Benutzer kann Datei auswählen und hochladen
- Die Datei wird analysiert von ein einfaches ML-Modell
- Resultat zeigt ob Datei ist "clean" oder "infected"

## 🛠️ Technologien benutzt:

- Python 3
- Flask (Web Framework)
- Scikit-learn (für Machine Learning)
- HTML / CSS für Oberfläche

## 🚀 Wie kann man starten?

1. Installiere alle Libraries:
    pip install -r requirements.txt
2. Starten Sie die App : 
    python app.py

3. Öffnen Sie `http://127.0.0.1:5000` in Browser

## 📁 Struktur vom Projekt

- `app.py` – Hauptdatei wo Flask läuft
- `templates/` – HTML Dateien
- `static/` – CSS Dateien
- `uploads/` – wo die hochgeladene Dateien gespeichert sind
- `model.pkl` – unser trainierte Modell

## 📝 Hinweis

Dies ist nur eine einfache Demonstration für Uni Projekt. Kein echte Antivirus oder Sicherheitsprogramm! Für Präsentation nur 😄
