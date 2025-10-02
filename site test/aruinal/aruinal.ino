int x = 0;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  while (Serial.available()){
    x = Serial.readString().toInt();
    Serial.println(x + 1);
  }
  
}
