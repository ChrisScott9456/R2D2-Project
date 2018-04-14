import RPi.GPIO as GPIO
from time import sleep
import subprocess

GPIO.setmode(GPIO.BCM)

Motor1F = 23
Motor1B = 24
Motor1E = 25
BLUE = 4
RED = 22

GPIO.setup(Motor1F, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

def play():
    subprocess.Popen(["omxplayer", "--vol", "-2000", "../R2D2/6.mp3"])

def forwards():
    GPIO.output(Motor1F, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

def backwards():
    GPIO.output(Motor1F, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

def blink():
    GPIO.output(BLUE, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    sleep(0.05)

print "Starting behavior 6"

play()
sleep(1.5)
for num in range(0,15):
    blink()

sleep(2)

print "Ending behavior 6"

GPIO.cleanup()
