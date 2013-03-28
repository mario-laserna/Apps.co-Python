def bienvenidos():
    print("Bienvenido a Agenda telefonica")
    print("Seleccione una opcion:")
    print("1-Annadir un registro a la agenda")
    print("2-Listar el contenido de la agenda")

def escribir():
    print("has elegido opcion 1 annadir")
    agenda = open("agenda_telefonica2.csv", 'a')
    posicion = input("Introduce la posicion: ")
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce su  telefono: ")
    agenda.write(posicion)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(telefono)
    agenda.write("\n")
    print("Se ha guardado en la agenda el contacto ", nombre,
          " con telefono ", telefono)
    agenda.close()

def listar(fin):
    print("has elegido opcion 2 listar")
    agenda = open("agenda_telefonica2.csv")
    numero = 0
    for i in range(1, fin):
        lectura = agenda.readline()
        print(lectura.replace(",", "\t\t"))
        numero = numero + 1
    agenda.close()

def mierror():
    print("opcion no valida")
