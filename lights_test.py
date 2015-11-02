import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED1 = 21
RED2 = 20
GREEN1 = 16
GREEN2 = 26
GREEN3 = 19

GPIO.setup(RED1, GPIO.OUT)
GPIO.setup(RED2, GPIO.OUT)
GPIO.setup(GREEN1, GPIO.OUT)
GPIO.setup(GREEN2, GPIO.OUT)
GPIO.setup(GREEN3, GPIO.OUT)


def light_off(index):
	GPIO.output(index, False)

def light_on(index):
	GPIO.output(index, True)

light_off(RED1)
light_off(RED2)
light_off(GREEN1)
light_off(GREEN2)
light_off(GREEN3)

time.sleep(1)

light_on(GREEN3)

time.sleep(1)

light_off(GREEN3)
light_on(GREEN2)

time.sleep(1)

light_off(GREEN2)
light_on(GREEN1)

time.sleep(1)

light_off(GREEN1)
light_on(RED2)

time.sleep(1)

light_off(RED2)
light_on(RED1)

time.sleep(1)

GPIO.cleanup()
