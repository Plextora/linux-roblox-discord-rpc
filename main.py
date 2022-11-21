from pypresence import Presence
import time
import psutil

start_time = time.time()
client_id = "1044302023211884624"
RPC = Presence(client_id)
RPC.connect()


def StartPresence():
    RPC.update(
        large_image="robloxicon",
        large_text="ROBLOX Icon",
        start=start_time,
    )


StartPresence()

print("Started presence!")

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)
    print("Reloaded presence!")
