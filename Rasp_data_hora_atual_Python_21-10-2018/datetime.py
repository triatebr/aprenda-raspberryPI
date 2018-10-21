import time
# Mostrar a data em formato DIA/MES/ANO
print (time.strftime('%d %b %y'))
# Mostrar a hora em formato HORAS:MINUTOS:SEGUNDOS
print (time.strftime('%H:%M:%S'))
print (time.strftime('%d/%m/%Y'))

# Mostrar + funções
print ("Data e hora atuais: ", time.ctime())
print ("Data e hora atuais com formato: ", time.strftime('%l:%M %p %Z on %b %d, %Y'))
print ("Ano atual: ", time.strftime("%Y"))
print ("Mês do ano: ", time.strftime("%B"))
print ("Número de semana do ano: ", time.strftime("%W"))
print ("Dia da semana: ", time.strftime("%w"))
print ("Dia do ano: ", time.strftime("%j"))
print ("Dia do mês: ", time.strftime("%d"))
print ("Dia da semana: ", time.strftime("%A"))

