import numpy as np
from joblib import load

# Загрузка обученной модели
model = load("model.pkl")

# Пример данных файла (признаки)
# [размер, количество функций, энтропия]
file_features = [350, 45, 180]  # заменишь на реальные данные

# Преобразуем в формат, подходящий модели
features = np.array(file_features).reshape(1, -1)

# Предсказание
prediction = model.predict(features)

# Вывод результата
if prediction[0] == 1:
    print("⚠️ Вредоносный файл")
else:
    print("✅ Файл безопасен")
