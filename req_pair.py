# coding: utf-8
import requests
import json

URL = "https://labs.goo.ne.jp/api/textpair"
payload = {"app_id":"d636e5a2778befad4a5c0b2d50b1544d1d1ca2b9e47dbe43c7c305c88a750999",
            "text1":"高橋さんはアメリカに出張に行きました。",
            "text2":"山田さんはイギリスに留学している。"
        }
res = requests.post(URL, headers={"Content-Type":"application/json"}, data=json.dumps(payload))
print(res.text)
