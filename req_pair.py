# coding: utf-8
import requests
import json

URL = "https://labs.goo.ne.jp/api/textpair"
payload = {"app_id":"240d3816ea7bdecfdc441f92acb20aba0a2d0651317de443ca10d16944222079",
            "text1":"高橋さんはアメリカに出張に行きました。",
            "text2":"山田さんはイギリスに留学している。"
        }
res = requests.post(URL, headers={"Content-Type":"application/json"}, data=json.dumps(payload))
print(res.text)
