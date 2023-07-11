import json
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

with open('your file path.json') as f:
    data = json.load(f)

# Извлечь значение поля "body"
body = data['body']
# Преобразовать строку "body" в объект Python
json_data = json.loads(body)

# Извлечь данные из объекта JSON
metrics = json_data['Metrics']
latency = metrics['Latency']

# Преобразовать данные в формат numpy array
X = np.array([1])  # Здесь представлен только один входной признак '1', вы можете добавить больше признаков
X = X.reshape(-1, 1)  # Изменить форму массива на двумерный
y = np.array([float(latency)])

# Создать модель GPR с выбранным ядром
kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

# Обучить модель на данных
gpr.fit(X, y)
print(metrics)

