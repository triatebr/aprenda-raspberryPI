import RPi.GPIO as GPIO, time
import RPi.GPIO as GPIO

 
#Declaração dos GPIO's da solução
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
 
#Código, valida-se as condições do Sensor
try:
    while True:
        if GPIO.input(18):
        	print("Sem Problemas de Vazamento de GÁS!")
        	time.sleep(3.0)
        if GPIO.input(18)!=1:
        	print("Cuidado! Vazamento de GÁS ....")
        	GPIO.output(27, False)
        	time.sleep(3.0)
        	GPIO.output(27, True)

#Final do Script
except KeyboardInterrupt:
    print ("See you later in #artDuino")
    GPIO.cleanup()
