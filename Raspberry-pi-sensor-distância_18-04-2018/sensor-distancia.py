#Programa: Sensor de distancia com Raspberry Pi B
#Autor: Lucas de Barros
 
# Carrega as bibliotecas
import RPi.GPIO as GPIO
import time
import requests
import json

# SETMODE diz como devemos referenciar os pinos da raspsberry
# usando o BCM usa o código de GPIO
# usando o 'BOARD usa o sequencial de 1 a 40'
# GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada 
GPIO.setmode(GPIO.BOARD)

#Define os pinos de conexão ao sensor
TRIG = 23
ECHO = 24

print ("Medição de Distância em andamento! Aguarde ...")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#while True: 
GPIO.output(TRIG, False)
print ("Aguardando o sensor...")
time.sleep(2)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)
print ("Distância:",distance,"cm")
GPIO.cleanup()
#time.sleep(10)
    
