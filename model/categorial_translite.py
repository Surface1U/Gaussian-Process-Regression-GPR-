import pandas as pd
import re

# https://pythonist.ru/polnoe-rukovodstvo-po-pandas-dlya-nachinayushhih/#column-cleanup
data = pd.read_csv('../metrics/data1.csv', sep=",")

print(data)

values = ["ON", "OFF", "all", "deleted"]

def str_col_remove(data, values):
    col_remove = []
    for col in data.columns:
        if data[col].isin(values).any():
            col_remove.append(col)
    data.drop(columns=col_remove, inplace=True)
    return data
data = str_col_remove(data, values)
print(data)

def del_previous(cell):
    if isinstance(cell, str) and re.search(r'Previous value : (\d+)', cell):
        numeric = re.findall(r'\d+', cell)
        return float(numeric[1])
    return cell

data = data.applymap(del_previous)

data.to_csv("../metrics/updated_data1.csv", index=False)
print(data)
print(data[["Innodb_log_file_size"]])
