from os import system
import requests , uuid , time 
import os
import time
from colorama import Fore, Back, Style
import sys
import json
import random


if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

req = requests.session()
uid = uuid.uuid4()
system("title " + "t.me/undecryptable")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print('')
print(Fore.CYAN + '          Critical Ops Report Bot by yin/who?')
print('')
print('')
userid = input(Back.BLACK + Fore.WHITE + "Enter UserID: ")
#bearer cookie is each report
#10 reports enough to ban new account for 2 days
#30 reports enough to ban old account for 2 days
while True:
    reports=[0,1,2]
    userids=[user id of reported acc,user id of reported acc]
    userid= random.choice(userids)
    auth=""#bearer tokens/account auth cookies
    rid = random.choice(reports)
    data = {"userid":userid,"reporttype":rid}
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'x-apiversion': '1.28.0.f1605',
        'authorization': auth,
        'content-length': '35',
        'x-unity-version': '2020.3.19f1',
        'accept-language': 'en-ca',
        'user-agent': 'CriticalOps/1765 CFNetwork/1128.0.1 Darwin/19.6.0',
        'accept-encoding': 'gzip, deflate, br',
        'Host': '1-28-0.prod.copsapi.criticalforce.fi'}
    url = "https://1-28-0.prod.copsapi.criticalforce.fi/api/user/report"
    res = requests.post(url,json=data,headers=headers)
    if res.status_code == 200:
        print(Fore.WHITE + "[" + Fore.MAGENTA + "+" + Fore.WHITE + "]" + Fore.MAGENTA + " Report sent!")
    else:
        print (Fore.RED + '[-] Error')
    if res.text == "Error 251":
        print(Fore.WHITE + "     " + "Report already sent.")
    else:
        print(Fore.WHITE + f"     Reported for {rid}")
    

#note from Timer1337: "play stupid games win stupid prizes."
#by yin/who?/timer/kevin
#0 is hacking etc
