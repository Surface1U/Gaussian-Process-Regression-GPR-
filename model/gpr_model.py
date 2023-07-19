import json
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import f1_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Загрузка данных из CSV без разделительных столбцов "|||"
data = pd.read_csv('../metrics/updated_data1.csv', sep=',', usecols=lambda col: '|||' not in col)
# print(data)

X = data.iloc[:, :-5]
y = data.iloc[:, -2]

# print(X)
# print(y)

X = X.values
y = y.values
# print(y)

kernel = RBF()
gpr = GaussianProcessRegressor(kernel=kernel)

gpr.fit(X, y)

# Обучить модель на данных
model_name = 'gpr_trained_model.joblib'
joblib.dump(gpr, model_name)
print("Saved model to disk")