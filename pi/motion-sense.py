import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

MotionSensor = 13

GPIO.setup(MotionSensor, GPIO.IN)
GPIO.setwarnings(False)

if (GPIO.input(MotionSensor) == 1:
  print ("Motion Sensor Activated")
