#define BLYNK_TEMPLATE_ID "TMPL4tSgmlhz9"
#define BLYNK_TEMPLATE_NAME "TTGO"
#define BLYNK_AUTH_TOKEN "TPMmy45ar_RbIYcCBh7arJ6qK92JeW0W"
#define BLYNK_HEARTBEAT 10

#include "utilities.h"
#include <Arduino.h>
#include <TinyGsmClient.h>
#include <BlynkSimpleTinyGSM.h>
#include <Stepper.h>

#define STEPPER_PIN_1 13
#define STEPPER_PIN_2 14
#define STEPPER_PIN_3 15
#define STEPPER_PIN_4 2

// Define stepper motor connections
const int stepsPerRevolution = 2048;  // Change this value according to your stepper motor
Stepper stepper(stepsPerRevolution, STEPPER_PIN_1, STEPPER_PIN_2, STEPPER_PIN_3, STEPPER_PIN_4);  // Stepper motor pins: IN1, IN2, IN3, IN4

BlynkTimer timer;
TinyGsm modem(SerialAT);

// Your GPRS credentials
// Leave empty, if missing user or pass
char apn[] = "internet";
char user[] = "";
char pass[] = "";
char pin[] = "6344";

// Variable to store the last angle value from V0
float lastAngle = 0.0;

// Blynk virtual pin V0 handler
BLYNK_WRITE(V0)
{
    float newAngle = param.asFloat();  // Get the new angle value from the Blynk app
    rotateStepper(newAngle);  // Rotate the stepper motor to the new angle
}

void setup()
{
    Serial.begin(115200);
    // Turn on DC boost to power on the modem
#ifdef BOARD_POWERON_PIN
    pinMode(BOARD_POWERON_PIN, OUTPUT);
    digitalWrite(BOARD_POWERON_PIN, HIGH);
#endif

    // Set modem reset pin, reset modem
    pinMode(MODEM_RESET_PIN, OUTPUT);
    digitalWrite(MODEM_RESET_PIN, !MODEM_RESET_LEVEL);
    delay(100);
    digitalWrite(MODEM_RESET_PIN, MODEM_RESET_LEVEL);
    delay(2600);
    digitalWrite(MODEM_RESET_PIN, !MODEM_RESET_LEVEL);

    // Turn on modem
    pinMode(BOARD_PWRKEY_PIN, OUTPUT);
    digitalWrite(BOARD_PWRKEY_PIN, LOW);
    delay(100);
    digitalWrite(BOARD_PWRKEY_PIN, HIGH);
    delay(1000);
    digitalWrite(BOARD_PWRKEY_PIN, LOW);

    // Set modem baud
    SerialAT.begin(115200, SERIAL_8N1, MODEM_RX_PIN, MODEM_TX_PIN);

    Serial.println("Modem powering up...");
    delay(3000);

    // Restart takes quite some time
    // To skip it, call init() instead of restart()
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

    // Set up the stepper motor
    stepper.setSpeed(3);  // Set stepper motor speed in RPM

    Serial.println("Blynk GSM Setup complete, ready to roll...");
}

void loop()
{
    Blynk.run();
    timer.run();
}

// Function to rotate the stepper motor to a specified angle
void rotateStepper(float angle)
{
    int stepsToMove = map(angle, 0, 360, 0, stepsPerRevolution);
    stepper.step(stepsToMove);
    lastAngle = angle;  // Update the last known angle
    digitalWrite(STEPPER_PIN_1,LOW);
    digitalWrite(STEPPER_PIN_2,LOW);
    digitalWrite(STEPPER_PIN_3,LOW);
    digitalWrite(STEPPER_PIN_4,LOW);  
}
