import numpy as np
from joblib import load

# Laden des trainierten Modells
model = load("model.pkl")

# Beispiel für Dateidaten (Zeichen)
# [Größe, Anzahl der Merkmale, Entropie]
file_features = [350, 45, 180]  # durch echte Daten ersetzen

# konvertieren es in ein für das Modell geeignetes Format
features = np.array(file_features).reshape(1, -1)

# Vorhersage
prediction = model.predict(features)

# Ausgabe des Ergebnisses
if prediction[0] == 1:
    print("⚠️ Вредоносный файл")
else:
    print("✅ Файл безопасен")
