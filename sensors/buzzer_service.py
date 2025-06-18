import grovepi
import time

buzzer = 7  # D7
grovepi.pinMode(buzzer, "OUTPUT")

while True:
    try:
        grovepi.digitalWrite(buzzer, 1)
        print("Buzzing...")
        time.sleep(1)
        grovepi.digitalWrite(buzzer, 0)
        time.sleep(1)
    except KeyboardInterrupt:
        break
