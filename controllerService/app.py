from flask import Flask, request

app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control_device():
    data = request.json
    device = data.get("device")
    action = data.get("action")

    print(f"Controlling {device}: {action}")
    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(port=5001)
