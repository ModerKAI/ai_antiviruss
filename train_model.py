import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

def generate_sample(is_malicious):
    if is_malicious:
        return [random.randint(100, 300), random.randint(100, 500), random.randint(10, 50)]
    else:
        return [random.randint(500, 2000), random.randint(0, 100), random.randint(100, 256)]

X = []
y = []

for _ in range(500):
    X.append(generate_sample(True))
    y.append(1)
for _ in range(500):
    X.append(generate_sample(False))
    y.append(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

dump(model, 'model.pkl')  # <--- важная строка
print("✅ Модель обучена и сохранена как model.pkl")

