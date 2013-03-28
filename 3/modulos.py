def bienvenidos():
    print("Bienvenido a Agenda telefonica")
    print("Seleccione una opcion:")
    print("1-Annadir un registro a la agenda")
    print("2-Listar el contenido de la agenda")
    print("3-Buscar por nombre en la agenda")

def escribir():
    print("has elegido opcion 1 annadir")
    
    #posicion = input("Introduce la posicion: ")
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce su  telefono: ")

    agenda = open("agenda_telefonica2.csv")
    for n in range(1,40):
        linea = agenda.readline()
        lineapartida = linea.split(",")
        if lineapartida[0] != "":
            memoria = lineapartida[0]
    agenda.close()

    print(memoria)
    
    posicion = str(int(memoria) + 1)
    agenda = open("agenda_telefonica2.csv", 'a')
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

def buscador(nombrebuscado):
    print("Buscando...")
    agenda = open("agenda_telefonica2.csv")
    for i in range(1, 30):
        lectura = agenda.readline()
        partido = lectura.split(",")
        if(partido[1] == nombrebuscado):
            print(partido[2])
    agenda.close()
