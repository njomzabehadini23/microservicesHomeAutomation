from flask import Flask, request
import datetime

app = Flask(__name__)
log_file = "sensor_log.txt"

@app.route("/log", methods=["POST"])
def log_sensor():
    data = request.json
    timestamp = datetime.datetime.now().isoformat()
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {data}\n")
    print(f"Logged sensor data: {data}")
    return {"logged": True}, 200

if __name__ == "__main__":
    app.run(port=5002)
