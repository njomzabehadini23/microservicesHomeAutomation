import grovepi
import time

sensor = 6  # D6

while True:
    try:
        [temp, humidity] = grovepi.dht(sensor, 0)  # 0 = blue DHT11, 1 = white DHT22
        print(f"Temp: {temp}C  Humidity: {humidity}%")
        time.sleep(2)
    except KeyboardInterrupt:
        break
