#Agenda telefonica

import modulos

modulos.bienvenidos()

opcion = input(">> ")

if opcion == "1":
    modulos.escribir()
elif opcion == "2":
    registros = int(input("Cuantos registros desea ver? ")) + 1
    modulos.listar(registros)
else:
    modulos.mierror()
