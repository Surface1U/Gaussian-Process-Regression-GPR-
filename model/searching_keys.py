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


path1 = 'D:/Leto/Data'
dd = 1
mm = 12
yyyy = 2022
listik = ["innodb_dedicated_server", "innodb_doublewrite_batch_size", "innodb_doublewrite_files", "innodb_doublewrite_pages", "innodb_log_files_in_group", "innodb_log_spin_cpu_abs_lwm", "innodb_log_spin_cpu_pct_hwm", "innodb_log_wait_for_flush_spin_hwm", "max_relay_log_size", "open_files_limit", "parser_max_mem_size", "relay_log_space_limit", "rpl_read_size", "stored_program_definition_cache", "tablespace_definition_cache", "temptable_max_ram"]

with open("data.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(listik)
    while True:
        try:
            path2 = to_dir(yyyy, mm, dd)
            path = path1 + "/" + path2
            for filename in glob.glob(os.path.join(path, '*.json')):
                with open(os.path.join(os.getcwd(), filename), 'r') as f:
                    print(filename)
                    json_str = f.read()
                    data = json.loads(json_str)
                    l = []
                    s2 = ""
                    for i in range(len(listik)):
                        try:
                            s1 = listik[i]
                            s2 = data[s1]
                            l.append(str(s2))
                        except:
                            l.append("nill")
                    if l != ["nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill", "nill"]:
                        file_writer.writerow(l)
                        print("!!!!!!!!")
            yyyy, mm, dd = add_day(yyyy, mm, dd)
        except:
            break

print("Done")
