import requests
import csv
import chardet
import json

with open("a.csv", "rb") as f:
    res = chardet.detect(f.read())
    enc = res["encoding"]

with open("a.csv", "r", encoding=enc) as f:
    reader = csv.reader(f)
    keywords = []
    for row in reader:
        lis = row[0].split("\t")
        keywords.append(lis[1])

for num, word in enumerate(keywords):
    URL = "https://labs.goo.ne.jp/api/textpair"
    payload = {"app_id":"d636e5a2778befad4a5c0b2d50b1544d1d1ca2b9e47dbe43c7c305c88a750999",
                "text1":word[0],
                "text2":word
            }
    res = requests.post(URL, headers={"Content-Type":"application/json"},
                        data=json.dumps(payload))
    res = json.loads(res.text)
