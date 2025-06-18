import grovepi
import time

sensor = 0  # A0
grovepi.pinMode(sensor, "INPUT")

while True:
    try:
        value = grovepi.analogRead(sensor)
        print("Light:", value)
        time.sleep(1)
    except KeyboardInterrupt:
        break
