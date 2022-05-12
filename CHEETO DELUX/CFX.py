from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA
os.system("cls")
os.system("title Python Example")
print("Initializing")
def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
    	path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest
keyauthapp = api(
	name = "svolf",
	ownerid = "U9zgiaTtnx",
	secret = "2f8c8505a69d35eae40b4b1852ecf4395d2c11504e0fc40ccbd2354b1a038ccb",
	version = "1.0",
	hash_to_check = getchecksum()
)
print ("""
1.Login
2.Register
3.Upgrade
4.License Key Only
""")
print(f"""
""")
ans=input("Select Option: ") 
if ans=="1": 
	user = input('Provide username: ')
	password = input('Provide password: ')
	keyauthapp.login(user,password)
elif ans=="2":
	user = input('Provide username: ')
	password = input('Provide password: ')
	license = input('Provide License: ')
	keyauthapp.register(user,password,license) 
elif ans=="3":
	user = input('Provide username: ')
	license = input('Provide License: ')
	keyauthapp.upgrade(user,license)
elif ans=="4":
	key = input('Enter your license: ')
	keyauthapp.license(key)
else:
	print("\nNot Valid Option") 
	sys.exit()

print("\nUser data: ") 
print("Loading in 10 secs....")
sleep(10)

import json
import os
import sys
import threading

from pynput import keyboard
from termcolor import colored


def on_release(key):
    try:
        if key == keyboard.Key.f1:
            Aimbot.update_status_aimbot()
        if key == keyboard.Key.f2:
            Aimbot.clean_up()
    except NameError:
        pass

def main():
    global lunar
    lunar = Aimbot(collect_data = "collect_data" in sys.argv)
    lunar.start()

def setup():
    path = "lib/config"
    if not os.path.exists(path):
        os.makedirs(path)

    print("[INFO] In-game X and Y axis sensitivity should be the same")
    def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)")
        return number

    xy_sens = prompt("X-Axis and Y-Axis Sensitivity (from in-game settings): ")
    targeting_sens = prompt("Targeting Sensitivity (from in-game settings): ")

    print("[INFO] Your in-game targeting sensitivity must be the same as your scoping sensitivity")
    sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}

    with open('lib/config/config.json', 'w') as outfile:
        json.dump(sensitivity_settings, outfile)
    print("[INFO] Sensitivity configuration complete")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

    print(colored('''

     _____ ________   __
     / ____|  ____\ \ / /
    | |    | |__   \ V / 
    | |    |  __|   > <  
    | |____| |     / . \ 
     \_____|_|    /_/ \_\
                      
                      


    (Doing The Magic)''', "magenta"))

    path_exists = os.path.exists("lib/config/config.json")
    if not path_exists or ("setup" in sys.argv):
        if not path_exists:
            print("[!] Sensitivity configuration is not set")
        setup()
    path_exists = os.path.exists("lib/data")
    if "collect_data" in sys.argv and not path_exists:
        os.makedirs("lib/data")
    from lib.aimbot import Aimbot
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    main()
    
    from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime

