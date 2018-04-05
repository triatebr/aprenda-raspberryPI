#Definindo da biblioteca GPIO
import RPi.GPIO as GPIO
from time import sleep

#Aqui definimos que vamos usar o numero de ordem do pino, e não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição "GPIO.BOARD (ex. Pino 12)" para "GPIO.BCM (ex.GPIO 18)" 
GPIO.setmode(GPIO.BOARD)

# Setando as portas de entrada e saída do LED1
ledPin = 7 #jumper do 1º resistor 1k
buttonPin = 11 #jumper do 1º button 

# Setando as portas de entrada e saída do LED2
ledPin2 = 29 #jumper do 2º resistor 1k
buttonPin2 = 33 #jumper do 2º button

#GPIO do LED1
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin, False)

#GPIO do LED2
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(ledPin2, False)


#Loop principal (Laço indefinido)
try:
    while(True):
        GPIO.output(ledPin, not GPIO.input(buttonPin))
        sleep(.1)
        GPIO.output(ledPin2, not GPIO.input(buttonPin2))
        sleep(.1)
finally:
    GPIO.output(ledPin, False)
    GPIO.output(ledPin2, False)
    GPIO.cleanup()
