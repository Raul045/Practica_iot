
# archivo.write("holaaaaaaaaaaa")
# n = int(input("Di cuantas veces deseas registrar nombres: "))
personas =[{
  "Nombre": "",
  "edad": "",
  "telefono": ""
}]
menu="""
--------Menu-----------
1.- Registrar Usuario |
2.- Mostrar           |
3.- Salir             |
-----------------------
"""
pop = True
while pop == True:
    archivo = open("laspruebas.txt","a")
    print(menu)
    opcion = input("Que deseas hacer: ")

    if opcion == "1":
        nombre = input("coloca el nombre porfavor: ")
        edad = input("Coloca tu edad: ")
        telefono = input("Coloca tu telefono: ")
        personas.update({"Nombre":nombre,"edad":edad,"telefono":telefono})
        archivo.write('personas=%s'%personas)
    
    elif opcion == "2":
        f = open("laspruebas.txt", "r")
        print(f.readline())
    
    elif opcion == "3":
        print("Hasta luego....")
        pop = False

    else:
        print("no vale esa opcion :(")

archivo.close()
