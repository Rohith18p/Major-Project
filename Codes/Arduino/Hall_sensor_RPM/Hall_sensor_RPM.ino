#define EO 134.4

#define dir1 7
#define pwm1 9
#define hall1 3 //extrernal Interrupt

volatile long encValue = 0;

int interval = 1000;
long previous = 0;
long current = 0;

int pwm = 0;
int rpm = 0;
boolean measure = false;

void setup() {
  Serial.begin(9600);

  pinMode(hall1, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(hall1), enc_update, RISING);

  pinMode(dir1, OUTPUT);
  pinMode(pwm1, OUTPUT);

  digitalWrite(dir1, HIGH);
  analogWrite(pwm1, 10);

  encValue = 0;
  previous = millis();
}

void loop() {
  current = millis();
  ///Serial.println(encValue);
  if(current - previous > interval){
    previous = current;
    rpm = (float)((encValue*60)/EO);

    if(rpm > 0) {
      Serial.print(encValue);
      Serial.print(" Pulses / ");
      Serial.print(EO);
      Serial.print(" * 60 (sec) = ");
      Serial.print(rpm);
      Serial.println(" RPM");
    }

    encValue = 0;
  }
}

void enc_update(){
  encValue++;
}
