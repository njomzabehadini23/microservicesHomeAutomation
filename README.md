# microservicesHomeAutomation
# Home Automation System using Microservices

This project implements a distributed **Home Automation System** using a **microservices architecture**. The system interacts with Arduino-controlled devices (such as lights and motion sensors) and handles tasks like device control, sensor logging, and notifications. It also demonstrates **fault tolerance** using AWS Lambda and CloudWatch.

## What I Built

I created a modular system where:
- Each service handles a specific task (device control, logging, notifications).
- Services communicate over HTTP or MQTT.
- Arduino devices detect motion and control lights.
- If a service fails, AWS triggers a serverless function to handle recovery or notify.

## Architecture Overview

**Microservices:**
- `controller-service/` – Turns lights/devices on/off based on input.
- `sensor-logger-service/` – Collects and logs data from motion/temperature sensors.
- `notification-service/` – Sends alerts based on sensor input (e.g., motion detected).
- `aws-fault-handler/` – CloudWatch + Lambda to detect failures and respond.

**Hardware:**
- Arduino Uno + sensors (e.g., motion, temperature).
- LED lights connected for automation actions.

**Cloud:**
- AWS Lambda for backup logic.
- AWS CloudWatch to monitor services.

## How to Run

### 1. Flash Arduino Sketch
- Upload code from `/arduino/` folder using the Arduino IDE.

### 2. Run Microservices
Start each service locally (or Dockerize them if needed):

```bash
cd controller-service
python app.py

cd ../sensor-logger-service
python app.py

cd ../notification-service
python app.py
