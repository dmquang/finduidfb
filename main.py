from typing import Union
from fastapi import FastAPI
import requests
import json
app = FastAPI()


@app.get("/")
def read_root():
    return {"main": "hello"}

def getinfo(link):
    headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(link, headers=headers).text
        name = response.split('<title>')[1].split('</title>')[0]
        uid = response.split('userID":"')[1].split('"')[0]
        return json.dumps({"TYPE": "SUCCESS" , "NAME" : name , "UID": uid})
    except:
        return json.dumps({"TYPE": "FAIL" , "MESAGE": "CAN NOT FIND USER!"})

@app.get("/link")
def read_item(link: str):
    return getinfo(link)
