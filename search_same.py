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
    payload = {"app_id":"240d3816ea7bdecfdc441f92acb20aba0a2d0651317de443ca10d16944222079",
                "text1":word[0],
                "text2":word
            }
    res = requests.post(URL, headers={"Content-Type":"application/json"},
                        data=json.dumps(payload))
    res = json.loads(res.text)
