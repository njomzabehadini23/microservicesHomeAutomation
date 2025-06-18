import time
from grove_rgb_lcd import *

while True:
    try:
        setText("Hello from\nGrove LCD!")
        setRGB(0, 128, 64)
        time.sleep(2)
        setText("Updated info...")
        setRGB(255, 0, 0)
        time.sleep(2)
    except KeyboardInterrupt:
        setText("")
        break
