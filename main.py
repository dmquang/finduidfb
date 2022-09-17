from typing import Union
from fastapi import FastAPI
import requests
import json
import uvicorn

app = FastAPI()

def follow(cookie,uid):
    try:
        csrftoken=cookie.split('csrftoken=')[1].split(';')[0]
        headers = {
            'authority': 'i.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-csrftoken': csrftoken,
        }
        checkacc = requests.get('https://www.instagram.com/', headers=headers).text
        try:
            idac = checkacc.split('viewerId":"')[1].split('"')[0]
            response = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{uid}/follow/',headers=headers)
            return json.dumps({"type":"FollowSuccess", "FollowUid": uid, "FollowBy": idac})
            sleep(2)
        except:
            return json.dumps({"type":"Fail", "mesage":"CookieIsNotValid!"})
    except:
        return json.dumps({"type":"Fail", "mesage":"CookieIsNotValid!"})


@app.get("/")
def Home():
    return json.dumps({"DARLING": "hello"})

@app.get("/follow")
def Follow(cookie: str,uid: str):
    return follow(cookie,uid)



