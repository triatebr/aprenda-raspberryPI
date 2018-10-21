#import commands
  
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    #Mostrar temperatura en grados Fahrenheit
    #return float(1.8*cpu_temp)+32
def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( 'C', '' )
    return  float(gpu_temp)
    #Mostrar temperatura em graus Fahrenheit
    # return float(1.8* gpu_temp)+32
def main():
    print("Temperatura CPU: ", str(get_cpu_temp()))
    print("Temperatura GPU: ", str(get_gpu_temp()))  
if __name__ == '__main__':
    main()
