#Agenda telefonica

import modulos

def principal():
    modulos.bienvenidos()

    opcion = input(">> ")

    if opcion == "1":
        modulos.escribir()
        principal()
    elif opcion == "2":
        registros = int(input("Cuantos registros desea ver? ")) + 1
        modulos.listar(registros)
        principal()
    elif opcion == "3":
        nombrebuscado = input("Nombre a buscar? ")
        modulos.buscador(nombrebuscado)
        principal()
    else:
        modulos.mierror()
        principal()

principal()
