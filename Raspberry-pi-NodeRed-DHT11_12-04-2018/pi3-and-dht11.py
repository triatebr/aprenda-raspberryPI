# Programa : Sensor de temperatura DHT11 com Raspberry Pi B+
# Autor : Lucas de Barros
 
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import requests
import json
from datetime import datetime

#Define varíavel de data e hora
now = datetime.now()

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor,
pino_sensor = 25
 
# Informacoes iniciais
 
while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pino_sensor)
    #date = time.strftime('%d %b %y')
    hora = time.strftime('%H:%M:%S')
    date = time.strftime('%d/%m/%Y')
    data = {'data':date,'hora':hora, 'humidity':humidity,'temperature':temperature}
    json_data = json.dumps(data)
    r = requests.post('http://192.168.11.112:1880/payload',json_data)
    print ("Data: ", time.strftime('%d/%m/%Y') ,"Time: ", time.strftime('%H:%M:%S'), ' Temp: {0:0.2f} C  Humidity: {1:0.2f} %'.format(temperature, humidity))
    time.sleep(20)
