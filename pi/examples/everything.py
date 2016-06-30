# Script thanks to Brett Farkas: https://youtu.be/1oIWW5d-0CA

import time
from datetime import datetime

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
MotionSensor = 13
GPIO.setup(MotionSensor, GPIO.IN)
GPIO.setwarnings(False)

import pygame
pygame.init()
pygame.mixer.init()

while (1):
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  day = datetime.today().weekday()

  if hour == 7 and minute = >= 0 and day < 5:
    if (GPIO.input(MotionSensor) == 1:
      pygame.mixer.music.load("GoodMorning.ogg")
      pygame.mixer.music.play()

      playing = pygame.mixer.music.get_busy()
      while (playing == 1):
        playing = pygame.mixer.music.get_busy()

