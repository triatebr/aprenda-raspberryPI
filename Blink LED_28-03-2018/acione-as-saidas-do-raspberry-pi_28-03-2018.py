#define o tempo que o led ficara aceso ou apagado
tempo=1
#Define biblioteca da GPIO
import RPi.GPIO as GPIO

#Define biblioteca de tempo
import time
GPIO.setmode(GPIO.BOARD)

#Define o pino 31 da placa como saida
GPIO.setup(31, GPIO.OUT)

#rotina para acender o led
def acendeled(pino_led):
    GPIO.output(pino_led, 1)
    return

#rotina para apagar o led
def apagaled(pino_led):
    GPIO.output(pino_led, 0)
    return

#Inicia loop
while(1):
    #Acende o led
    acendeled(31)
    #Aguarda segundo
    time.sleep(tempo)
    #apaga o led
    apagaled(31)
    #Aguarda meio segundo e reinicia o processo
    time.sleep(tempo)
