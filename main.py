from pypresence import Presence
import time
import psutil
import os

start_time = time.time()
client_id = "1044302023211884624"
rpc = Presence(client_id)
rpc.connect()
other_process_name = "robloxplayerbet"
main_process_name = "robloxplayerbeta"


def start_presence():
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


start_presence()

print("Started presence!")

while True:
    if if_roblox_running():
        start_presence()
    else:
        rpc.clear()
        start_time = time.time()  # reset the time elapsed field in rpc
    time.sleep(1)
    print("Reloaded presence!")
