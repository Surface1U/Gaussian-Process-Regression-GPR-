import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Загрузка данных из CSV файла
# data = pd.read_csv("C:/Users/Alexander/SummerPractice2023/SummerPractice2023/test_data/test1.csv")
data = pd.read_csv('C:/Users/Alexander/SummerPractice2023/SummerPractice2023/test_data/test1.csv', delimiter=";")

# Извлечение признаков (всех столбцов, кроме последнего) и целевой переменной (последнего столбца)
X = data.iloc[:, :12]
y = data.iloc[:, 12]

# Разделение данных на обучающую и тестовую выборки (80% обучающих данных, 20% тестовых данных)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели GPR с выбранным ядром
kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

# Обучение модели на обучающих данных
gpr.fit(X_train, y_train)

# Оценка производительности модели на тестовых данных
score = gpr.score(X_test, y_test)
print("Score on test data:", score)
