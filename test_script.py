import requests
import json
from flask import Markup
RUN_URL = 'http://13.233.71.241/compile/'

code = "print('Hello World!')"
lang = "PYTHON"
inp = ""
run_id = 0

data = {
    "code": code,
    "lang": lang,
    "input": inp,
    "id": run_id
}

data = json.dumps(data)
r = requests.post(RUN_URL, data=data)
output = Markup(json.loads(r.json()))
print(output)
