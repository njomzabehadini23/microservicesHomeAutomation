from flask import Flask, request

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    print(f"Notification: {data.get('message')}")
    return {"notified": True}, 200

if __name__ == "__main__":
    app.run(port=5003)
