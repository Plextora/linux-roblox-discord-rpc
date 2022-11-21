from pypresence import Presence
import time
import psutil
import os

start_time = time.time()
client_id = "1044302023211884624"
RPC = Presence(client_id)
RPC.connect()
otherProcessName = "robloxplayerbet"
mainProcessName = "robloxplayerbeta"


def StartPresence():
    RPC.update(
        large_image="robloxicon",
        large_text="ROBLOX Icon",
        start=start_time,
    )


def IfRobloxRunning():
    for proc in psutil.process_iter():
        try:
            if mainProcessName.lower() in proc.name().lower():
                return True
            elif otherProcessName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


StartPresence()

print("Started presence!")

while True:
    if IfRobloxRunning():
        StartPresence()
    else:
        RPC.clear()
    time.sleep(1)
    print("Reloaded presence!")
