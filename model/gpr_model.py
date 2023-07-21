import pandas as pd
import numpy as np
<<<<<<< Branchless
import pandas as pd
import joblib
from sklearn.metrics import f1_score
=======
from sklearn.model_selection import train_test_split
>>>>>>> main
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import csv
# Загрузка данных из CSV без разделительных столбцов "|||"
data = pd.read_csv('../metrics/updated_data1.csv', sep=',', usecols=lambda col: '|||' not in col)
# print(data)

X = data.iloc[:, :-5]
y = data.iloc[:, -2]
X = X.values
y = y.values

kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

gpr.fit(X, y)
# Обучить модель на данных
model_name = 'gpr_trained_model.joblib'
joblib.dump(gpr, model_name)
print("Saved model to disk")
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

