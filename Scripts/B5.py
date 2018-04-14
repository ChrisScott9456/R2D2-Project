import RPi.GPIO as GPIO
from time import sleep
import pygame
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
GPIO.setup(RED, GPIO.OUT)

def play():
    subprocess.Popen(["omxplayer", "--vol", "-2000",  "../R2D2/5.mp3"])

def forwards():
    GPIO.output(Motor1F, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

def backwards():
    GPIO.output(Motor1F, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

print "Starting behavior 5"

GPIO.output(RED, GPIO.HIGH)
play()
GPIO.output(RED, GPIO.LOW)
sleep(2)
GPIO.output(RED, GPIO.HIGH)
forwards()
sleep(0.2)
backwards()
sleep(0.2)
forwards()
sleep(0.2)
backwards()
sleep(0.2)
forwards()
sleep(0.2)
backwards()
sleep(0.2)
forwards()
sleep(0.2)
backwards()
sleep(0.2)

print "Ending behavior 5"
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()
