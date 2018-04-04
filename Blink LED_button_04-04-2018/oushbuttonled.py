# -*- coding: utf-8 -*-
#Definindo da biblioteca GPIO
import RPi.GPIO as GPIO
from time import sleep

#Aqui definimos que vamos usar o numero de ordem do pino, e não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição "GPIO.BOARD (ex. Pino 12)" para "GPIO.BCM (ex.GPIO 18)" 
GPIO.setmode(GPIO.BOARD)

# Setando as portas de entrada e saída
ledPin = 7
buttonPin = 11
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, False)

#Loop principal (Laço indefinido)
try:
    while(True):
        GPIO.output(ledPin, not GPIO.input(buttonPin))
        sleep(.1)
finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup()
