import csv
import json
import os
import glob

def add_day(yyyy, mm, dd):
    dd += 1
    if dd > 27:
        if yyyy % 4 == 0:
            feb = 29
        else:
            feb = 28
        if (dd == feb + 1 and mm == 2):
            mm = 3
            dd = 1
        elif dd == 31 and ((mm % 2 == 1 and mm > 8) or (mm % 2 == 0 and mm < 8)):
            mm += 1
            dd = 1
        elif dd == 32:
            mm += 1
            dd = 1
        if mm == 13:
            yyyy += 1
            mm = 1
    return yyyy, mm, dd

def to_dir(yyyy, mm, dd):
    if dd < 10:
        dds = "0" + str(dd)
    else:
        dds = str(dd)
    if mm < 10:
        mms = "0" + str(mm)
    else:
        mms = str(mm)
    return str(yyyy) + "-" + str(mms) + "-" + str(dds)

path1 = 'your path/json'
dd = 21
mm = 1
yyyy = 2023
listik = [
    "Metrics.Latency",
    "Status.Aborted_clients",
    "Status.Aborted_connects",
    "Status.Acl_cache_items_count",
    "Status.Binlog_cache_disk_use",
    "Status.Binlog_cache_use",
    "Status.Binlog_stmt_cache_disk_use",
    "Status.Binlog_stmt_cache_use"
]


with open("data.csv", mode="w", encoding='utf-8', newline='') as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    file_writer.writerow(listik)
    while True:
        try:
            path2 = to_dir(yyyy, mm, dd)
            path = os.path.join(path1, path2)
            for filename in glob.glob(os.path.join(path, '*.json')):
                with open(filename, 'r') as f:
                    print(filename)
                    json_str = f.read()
                    data = json.loads(json_str)
                    row_data = []
                    for item in listik:
                        keys = item.split('.')
                        value = data
                        for key in keys:
                            if key in value:
                                value = value[key]
                            else:
                                value = None
                                break
                        if value is not None:
                            row_data.append(str(value))
                        else:
                            row_data.append("nill")
                    file_writer.writerow(row_data)
                    print("!!!!!!!!")
            yyyy, mm, dd = add_day(yyyy, mm, dd)
        except:
            break

print("Done")
