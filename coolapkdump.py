import requests
import json
from pprint import pprint as pp
import threading
from time import time
from hashlib import md5
from base64 import b64encode as b64

uid = 1290253
url = 'https://api.coolapk.com/v6/user/feedList?uid='


def ordersandwich():
    time1 = int(time())
    sandwich = md5(b64(('token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?'+md5(str(time1).encode()).hexdigest()+'$00000000-0000-0000-0000-000000000000&com.coolapk.market').encode())).hexdigest()+'00000000-0000-0000-0000-000000000000'+hex(time1)
    return sandwich


i = 0
while True:
    i += 1
    headers = {
        "User-Agent": "+CoolMarket/9.0.2",
        "X-App-Id": "com.coolapk.market",
        "X-Requested-With": "XMLHttpRequest",
        "X-App-Version": "9.0.2",
        "X-App-Code": "1902151",
        "X-App-Token": ordersandwich(),
        "Cookie": ""
    }
    response = requests.get(url+str(uid)+'&page='+str(i), headers=headers)
    if len(json.loads(response.text)) > 0:
        with open('feedlist_u'+str(uid)+'p'+str(i)+'.json','w') as file:
            file.write(response.text)
        print(i)
    else:
        break