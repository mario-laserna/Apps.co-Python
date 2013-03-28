agenda = open("agenda_telefonica2.csv")

#print(agenda.read())

#print(agenda.readline())
#print(agenda.readline())

##print("Iniciando con for")
##
##for i in range(0,11):
##    print(agenda.readline())
##
##print("Ya he terminado")

numero = 0
while numero < 25:
    print(agenda.readline())
    numero = numero + 1
