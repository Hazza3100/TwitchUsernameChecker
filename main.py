import os
import random
import string
import requests
import threading
from colorama import Fore

class stats():
    alive = 0
    taken = 0
    checked = 0

def check():
    os.system(f"title Twitch User Check ^| Available: {stats.alive} ^| Taken: {stats.taken} ^| Checked: {stats.checked}")
    username = "".join(random.SystemRandom().choice(string.ascii_lowercase)for _ in range(4))

    headers = {
        'Accept': '*/*','Accept-Language': 'en-GB','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','Connection': 'keep-alive','Content-Type': 'text/plain;charset=UTF-8','Origin': 'https://www.twitch.tv','Referer': 'https://www.twitch.tv/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}

    data = '[{"operationName":"UsernameValidator_User","variables":{"username":"'+username+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'

    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    res = r.json()[0]["data"]["isUsernameAvailable"]
    if res == True:
        stats.alive += 1
        stats.checked += 1
        print(f"{Fore.GREEN}+{Fore.RESET} [{username}]")
        open('available.txt', 'a').write(f"{username}\n")
    else:
        stats.taken += 1
        stats.checked += 1
        print(f"{Fore.RED}-{Fore.RESET} [{username}]")




os.system('cls')
threads = int(input("Threads > "))
for _ in range(threads):
    threading.Thread(target=check).start()
