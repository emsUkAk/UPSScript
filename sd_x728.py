#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os  # Import os to run system commands

PLD_PIN = 6
BUZZER_PIN = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLD_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

while True:
    i = GPIO.input(PLD_PIN)
    if i == 0:
        print("AC Power OK")
        GPIO.output(BUZZER_PIN, 0)
    elif i == 1:
        print("Power Supply A/C Lost")
        GPIO.output(BUZZER_PIN, 1)
        time.sleep(1)  # Small delay before shutdown
        print("Shutting down the system...")
        os.system("source ~/.bashrc")
        os.system("x728off")  # Shutdown command
        break  # Exit the loop after shutdown command
        
    time.sleep(1)
