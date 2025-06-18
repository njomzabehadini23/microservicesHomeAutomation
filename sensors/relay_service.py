import grovepi
import time

relay = 4  # D4
grovepi.pinMode(relay, "OUTPUT")

while True:
    try:
        grovepi.digitalWrite(relay, 1)
        print("Relay ON")
        time.sleep(2)
        grovepi.digitalWrite(relay, 0)
        print("Relay OFF")
        time.sleep(2)
    except KeyboardInterrupt:
        break
