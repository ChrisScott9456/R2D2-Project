import RPi.GPIO as GPIO
from time import sleep
import pygame

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
GPIO.setup(BLUE, GPIO.OUT)

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("../R2D2/4.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def forwards():
    GPIO.output(Motor1F, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

def backwards():
    GPIO.output(Motor1F, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

def blink():
    GPIO.output(RED, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BLUE, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.LOW)
    

print "Starting behavior 4"

forwards()
sleep(0.5)
GPIO.output(Motor1E, GPIO.LOW)
sleep(1)
blink()
play()
blink()
sleep(0.05)
blink()
sleep(0.05)
backwards()
sleep(0.5)

print "Ending behavior 4"
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()
