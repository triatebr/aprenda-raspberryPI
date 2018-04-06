# Programa : Sensor de temperatura DHT11 com Raspberry Pi B+
# Autor : Lucas de Barros
 
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import requests
import json
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
 
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor,
pino_sensor = 25
 
# Informacoes iniciais
 
while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pino_sensor)
    data = {'humidity':humidity,'temperature':temperature}
    #json_data = json.dumps(data)
    #r = requests.post('http://192.168.11.112:1880/payload',json_data)
    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    time.sleep(2)
