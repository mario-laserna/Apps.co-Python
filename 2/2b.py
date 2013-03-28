agenda = open("agenda_telefonica.csv", 'a')
#print(agenda.read())
#agenda.truncate()
#agenda.write("Esto es algo de contenido que estoy escribiendo")

nombre = input("Introduce el nombre del contacto: ")
telefono = input("Introduce su  telefono: ")

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write("\n")

print("Se ha guardado en la agenda el contacto ", nombre,
      " con telefono ", telefono)


agenda.close()
