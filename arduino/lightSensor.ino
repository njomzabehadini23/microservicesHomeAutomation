int motionPin = 2;     // PIR motion sensor
int ledPin = 13;       // Built-in LED

void setup() {
  pinMode(motionPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int motion = digitalRead(motionPin);
  if (motion == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Motion detected!");
    delay(500);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
