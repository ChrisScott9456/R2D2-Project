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

def play():
    subprocess.Popen(["omxplayer", "--vol", "-2000", "../R2D2/7.mp3"])

def forwards():
    GPIO.output(Motor1F, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

def backwards():
    GPIO.output(Motor1F, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

def blink():
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    GPIO.output(BLUE, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)
    sleep(0.5)

print "Starting behavior 7"
backwards()
sleep(1)
GPIO.output(Motor1E, GPIO.LOW)
play()
sleep(2)
blink()
sleep(1)
forwards()
sleep(1)

print "Ending behavior 7"

GPIO.cleanup()
