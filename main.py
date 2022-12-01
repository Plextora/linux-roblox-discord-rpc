#!/usr/bin/python3

import re
from pypresence import Presence
import time
import psutil
import os
import platform
import requests

if platform.system() != "Linux":
    print(
        "linux-roblox-discord-rpc is made for Linux (duh)! But it seems like you're running on a different OS."
    )
    print(
        "linux-roblox-discord-rpc will (probably) not work at all for you, and you'll have absolutely ZERO support for any problems that come up!"
    )
    print("Do you still want to continue? (y/n)")
    decision = input("")
    if decision == "n":
        os._exit(1)

start_time = time.time()
client_id = 1044302023211884624
rpc = Presence(client_id)
rpc.connect()
other_process_name = "robloxplayerbet"
main_process_name = "robloxplayerbeta"


def get_current_game():
    if if_roblox_running():
        place_id_regex = re.compile(r"placeId=(\d+)")
        for process in psutil.process_iter():
            place_id_string = place_id_regex.search(
                " ".join(process.cmdline()))
            if place_id_string:
                if place_id_string != "":
                    place_id = place_id_string.group().replace("placeId=", "")
                    # wacky regex shenanigans, I might clean this up in the future but for now im just done with regex.

        response = requests.get(
            "https://api.roblox.com/marketplace/productinfo?assetId=" + place_id
        )

        try:
            return response.json()["Name"]
        except:
            if response.status_code == 429:
                print("Rate limited!")
            return "Program is being rate limited!"


def start_presence():
    current_game = get_current_game()
    if current_game != "Program is being rate limited!":
        rpc.update(
            large_image="robloxicon",
            large_text="ROBLOX Icon",
            start=start_time,
            state=f"Playing {current_game}",
        )
    else:
        rpc.update(
            large_image="robloxicon",
            large_text="ROBLOX Icon",
            start=start_time,
        )


def if_roblox_running():
    for proc in psutil.process_iter():
        try:
            if main_process_name.lower() in proc.name().lower():
                return True
            elif other_process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


print("Starting presence! The presence will reload every 15 seconds.\nThis is because of ROBLOX's rate limiting on API requests.\n")

while True:
    if if_roblox_running():
        start_presence()
    else:
        rpc.clear()
        start_time = time.time()  # reset the time elapsed field in rpc
    time.sleep(15)
    print("Reloaded presence!")
