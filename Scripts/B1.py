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
GPIO.setup(BLUE, GPIO.OUT)

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("../R2D2/1.mp3")
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

print "Starting behavior 1"

forwards()
play()
GPIO.output(BLUE, GPIO.HIGH)

sleep(0.2)

backwards()

sleep(2)

print "Ending behavior 1"
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()
