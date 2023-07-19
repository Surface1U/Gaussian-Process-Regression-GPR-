import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import csv

# Загрузка данных из CSV файла
# data = pd.read_csv("C:/Users/Alexander/SummerPractice2023/SummerPractice2023/test_data/test1.csv")
data = pd.read_csv('C:/Users/Alexander/SummerPractice2023/data.csv', delimiter=";")

# Извлечение признаков (всех столбцов, кроме последнего) и целевой переменной (последнего столбца)
#test1
# X = data.iloc[:, :12]
# y = data.iloc[:, 12]
#test2
# X = data.iloc[:, 14:92]  # Извлечь все строки и столбцы с 14 по 85
# y = data.iloc[:, 14:92]

# # #test3
# X = data.iloc[:, 93:105]  # Извлечь все строки и столбцы с 14 по 85
# y = data.iloc[:, 93:105]

# #test4
X = data.iloc[:, 106:121]
y = data.iloc[:, 106:121]

# Создать модель GPR с выбранным ядром
kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

# Обучить модель на данных
gpr.fit(X, y)

# Вывести гиперпараметры модели
with open("output.csv", mode="w", encoding="utf-8", newline='') as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    file_writer.writerow(["Hyperparameters"])
    for hyperparameter in gpr.kernel_.get_params():
        file_writer.writerow([str(hyperparameter)])

    file_writer.writerow([])
    file_writer.writerow(["Covariance Function"])
    covariance_matrix = gpr.kernel_(X)
    for i in range(len(covariance_matrix)):
        file_writer.writerow(covariance_matrix[i])

    file_writer.writerow([])
    file_writer.writerow(["Predictions"])
    predictions, std = gpr.predict(X, return_std=True)
    for i in range(len(X)):
        file_writer.writerow([predictions[i], std[i]])

print("Done")




