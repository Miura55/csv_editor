import csv
import chardet

with open("a.csv", "rb") as f:
    res = chardet.detect(f.read())
    enc = res["encoding"]

with open("a.csv", "r", encoding=enc) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        lis = row[0].split("\t")
        print(lis[1])
