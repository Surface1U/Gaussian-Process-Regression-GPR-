import json
import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import csv
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

# Загрузка данных из CSV файла
# data = pd.read_csv("C:/Users/Alexander/SummerPractice2023/SummerPractice2023/test_data/test1.csv")
data = pd.read_csv('C:/Users/honor/OneDrive/Рабочий стол/Practice/datasets/data.csv', delimiter=";")

# Извлечение признаков (всех столбцов, кроме последнего) и целевой переменной (последнего столбца)
#test1
# X = data.iloc[:, :12]
# y = data.iloc[:, 12]
#test2
X = data.iloc[:, 14:92]  # Извлечь все строки и столбцы с 14 по 85
y = data.iloc[:, 14:92]

# # #test3
# X = data.iloc[:, 93:105]  # Извлечь все строки и столбцы с 14 по 85
# y = data.iloc[:, 93:105]

# #test4
# X = data.iloc[:, 106:121]
# y = data.iloc[:, 106:121]


kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

# Fit the model on the data
gpr.fit(X, y)

# Get the optimal hyperparameters of the kernel
print("Optimal kernel hyperparameters:")
print("Length Scale:", gpr.kernel_.length_scale)

# Get the negative log likelihood of the model
print("Negative Log Likelihood:", -gpr.log_marginal_likelihood_value_)

# Get the speed of convergence of the parameter estimates
print("Speed of convergence of parameter estimates:", gpr.kernel_.length_scale / gpr.kernel_.length_scale)

# Calculate the predictions for a slightly perturbed length scale
perturbed_length_scale = gpr.kernel_.length_scale * 1.1
gpr_perturbed = GaussianProcessRegressor(kernel=RBF(length_scale=perturbed_length_scale))
gpr_perturbed.fit(X, y)
perturbed_predictions = gpr_perturbed.predict(X)

# Calculate the speed of convergence of the predictions
prediction_convergence_speed = np.mean(np.abs(perturbed_predictions - gpr.predict(X)) / np.abs(perturbed_length_scale - gpr.kernel_.length_scale))
print("Speed of convergence of predictions:", prediction_convergence_speed.round(4))

# Функция для построения кривой обучения
def plot_learning_curve(estimator, X, y, cv=None, train_sizes=np.linspace(0.1, 1.0, 5)):
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, train_sizes=train_sizes,
                                                            scoring='neg_mean_squared_error', n_jobs=-1)

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, color='blue', marker='o', markersize=5, label='Training MSE')
    plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std, alpha=0.15, color='blue')
    plt.plot(train_sizes, test_mean, color='green', linestyle='--', marker='s', markersize=5, label='Validation MSE')
    plt.fill_between(train_sizes, test_mean + test_std, test_mean - test_std, alpha=0.15, color='green')
    plt.xlabel('Number of Training Samples')
    plt.ylabel('Negative Mean Squared Error')
    plt.legend(loc='lower right')
    plt.show()

# Построение кривой обучения
plot_learning_curve(gpr, X, y, cv=5)
