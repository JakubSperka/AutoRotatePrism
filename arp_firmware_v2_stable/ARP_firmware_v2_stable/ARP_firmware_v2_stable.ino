#define BLYNK_TEMPLATE_ID "TMPL4tSgmlhz9"
#define BLYNK_TEMPLATE_NAME "TTGO"
#define BLYNK_AUTH_TOKEN "TPMmy45ar_RbIYcCBh7arJ6qK92JeW0W"
#define BLYNK_HEARTBEAT 10

#include "utilities.h"
#include <Arduino.h>
#include <TinyGsmClient.h>
#include <BlynkSimpleTinyGSM.h>
#include <Stepper.h>
#include <DHT.h>

#define STEPPER_PIN_1 13
#define STEPPER_PIN_2 14
#define STEPPER_PIN_3 15
#define STEPPER_PIN_4 2
#define DHT_PIN 32
#define DHTTYPE DHT11

const int stepsPerRevolution = 2048;
Stepper stepper(stepsPerRevolution, STEPPER_PIN_1, STEPPER_PIN_2, STEPPER_PIN_3, STEPPER_PIN_4);

BlynkTimer timer;
TinyGsm modem(SerialAT);
DHT dht(DHT_PIN, DHTTYPE);

char apn[] = "internet";
char user[] = "";
char pass[] = "";
char pin[] = "6344";

float lastAngle = 0.0;

void sendSensorData()
{
    float temperature = dht.readTemperature();  // Read temperature in Celsius
    float humidity = dht.readHumidity();        // Read humidity

    if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }

    Blynk.virtualWrite(V1, temperature);  // Send temperature to V1
    Blynk.virtualWrite(V2, humidity);     // Send humidity to V2
}

BLYNK_WRITE(V0)
{
    float newAngle = param.asFloat();
    rotateStepper(newAngle);
}

void setup()
{
    Serial.begin(115200);

    pinMode(MODEM_RESET_PIN, OUTPUT);
    digitalWrite(MODEM_RESET_PIN, !MODEM_RESET_LEVEL);
    delay(100);
    digitalWrite(MODEM_RESET_PIN, MODEM_RESET_LEVEL);
    delay(2600);
    digitalWrite(MODEM_RESET_PIN, !MODEM_RESET_LEVEL);

    pinMode(BOARD_PWRKEY_PIN, OUTPUT);
    digitalWrite(BOARD_PWRKEY_PIN, LOW);
    delay(100);
    digitalWrite(BOARD_PWRKEY_PIN, HIGH);
    delay(1000);
    digitalWrite(BOARD_PWRKEY_PIN, LOW);

    SerialAT.begin(115200, SERIAL_8N1, MODEM_RX_PIN, MODEM_TX_PIN);

    Serial.println("Modem powering up...");
    delay(3000);

    Serial.println("Initializing modem...");
    if (!modem.init())
    {
        Serial.println("Failed to restart modem, delaying 10s and retrying");
        return;
    }

    String name = modem.getModemName();
    Serial.println("Initialized Modem: " + name);

    modem.simUnlock(pin);

    Blynk.begin(BLYNK_AUTH_TOKEN, modem, apn, user, pass);

    stepper.setSpeed(3);

    dht.begin();
    timer.setInterval(10000L, sendSensorData);  // Send sensor data every 10 seconds

    Serial.println("Blynk GSM Setup complete, ready to roll...");
}

void loop()
{
    Blynk.run();
    timer.run();
}

void rotateStepper(float angle)
{
    int stepsToMove = map(angle, 0, 360, 0, stepsPerRevolution);
    stepper.step(stepsToMove);
    lastAngle = angle;

    digitalWrite(STEPPER_PIN_1, LOW);
    digitalWrite(STEPPER_PIN_2, LOW);
    digitalWrite(STEPPER_PIN_3, LOW);
    digitalWrite(STEPPER_PIN_4, LOW);
}
