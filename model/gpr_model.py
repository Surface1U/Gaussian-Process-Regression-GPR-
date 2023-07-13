import json
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

with open('C:/Users/Alexander/Desktop/storage/json/2023-01-21/0ddcaee1-74d9-4291-88d3-6c0b877a83d9.json') as f:
    data = json.load(f)

body = data['body']
# Преобразовать строку "body" в объект Python
json_data = json.loads(body)

# Извлечь данные из объекта JSON
metrics = json_data['Metrics']
latency = metrics['Latency']
innodb_doublewrite_files = metrics['innodb_doublewrite_files']

# Преобразовать данные в формат numpy array
X = np.array([2])  # Здесь представлен только один входной признак '1', вы можете добавить больше признаков
X = X.reshape(-1, 1)  # Изменить форму массива на двумерный
y = np.array([float(latency)], [float(innodb_doublewrite_files )])

# Создать модель GPR с выбранным ядром
kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

# Обучить модель на данных
gpr.fit(X, y)
print(metrics)
