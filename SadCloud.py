import os
import ctypes
import requests
import random
import string
import time
print("""
 ╔══════════════════════════════════════════════════╗
╔╝                                                  ╚╗
║    ╔═══════════════════════════════════════════╗   ║
║   ╔╝                                           ╚╗  ║
║  ╔╝              ██████                         ╚╗ ║
║  ║            ██████████   ██████                ║ ║
║  ║          ▓▓██████████▓▓████████▓▓             ║ ║
║  ║          ██████████████████████████           ║ ║
║  ║        ████████████████████████████           ║ ║
║  ║      ████████░░██░░████░░██░░██████           ║ ║
║  ║      ██████████░░████████░░████████████       ║ ║
║  ║    ███████████████████████████████████████    ║ ║
║  ║   ██████████████████░░░░██████████████████    ║ ║
║  ║   ████████████████░░████░░███████████████     ║ ║
║  ║    ███████████████████████████████████        ║ ║
║  ╚╗        ████████████████████████████         ╔╝ ║
║   ╚╗                                           ╔╝  ║
║    ╚═══════════════════════════════════════════╝   ║                                          
║              ╔══════════════════════╗              ║
║              ║  SadCloud Generator  ║              ║
║              ╚══════════════════════╝              ║
║    ╔═══════════════════════════════════════════╗   ║
║    ║Input How Many Codes to Generate and Check :   ║
║    ╚═══════════════════════════════════════════╝   ║
╚╗                                                  ╔╝
 ╚══════════════════════════════════════════════════╝
""")
num = int(input('>'))
with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 19
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generateing {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")


time.sleep(0.2)

input("\n Finished. valid codes in Valid Codes.txt, if empty then it diddnt find any, try running this again with a bigger number. ")

