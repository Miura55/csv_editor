import requests
import csv
import chardet
import json
import os

csv_list = [file_name for file_name in os.listdir("./") if ".csv" in file_name]
print(csv_list)

keywords = {}
with open("a.csv", "rb") as f:
    res = chardet.detect(f.read())
    enc = res["encoding"]

with open("a.csv", "r", encoding=enc) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        _keyword = row[0].split("\t")[1]
        if _keyword not in keywords.keys():
                keywords[_keyword] = 1

for data in csv_list[1:]:
    with open(data, "rb") as f:
        res = chardet.detect(f.read())
        enc = res["encoding"]

    with open(data, "r", encoding=enc) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            _keyword = row[1]
            if _keyword not in keywords.keys():
                keywords[_keyword] = 1
            else:
                keywords[_keyword] += 1

for k, v in sorted(keywords.items(), key=lambda x: x[1]):
    print(str(k) + ": " + str(v))
    