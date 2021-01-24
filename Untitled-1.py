import datetime

from clase_material import Material as material

from Clase_Persona import Persona 

from Clase_Accion import Prestamo as pre


m = material()
P = Persona()
Prestamos = pre()

def RegistrarNpersona():
    coas = P.Registro(nombres,edadn,telefonon)

def RegistrarNMaterial():
    mat = m.RegistroArticulo(nmaterial)

def RegistraNPrestamo(usu, materia, can):
    datosValidados = (usu,materia,can)
    fecha = str(datetime.datetime.now())
    prestamo = Prestamos.RegistroPrestamo(usu, materia, can, fecha)

def RegistrarNDevoluciones(folios):
    devolucion = Prestamos.RegistroDevolucion(folios)
    if devolucion:
      print('| Devolucion Exitosa | Que tenga buen dia')
    else: print('| Devolucion Fallida | Verifique su folio')

                

menu = """
|||---->Bievenido al centro deportivo<----||||
°A continuacion te mostraremos las opciones disponibles°
------->Menu<------------------
1.- Agregar usuario           |
2.- Informacion del sistema   |
3.- Agregar Material          |
4.- Ver Material              |
5.- Entregar Material         |
6.- Recibir Material          |
7.- Informacion               |
8.- Salir                     |
-------------------------------
"""
pop = True
while pop == True:
    print(menu)
    opcion = input("Elige la opcion que gustes: ")
    
    if opcion == "1":
        print("------------------------------")
        print("->Agregar Usuario<-")
        nombres = input("Nombre de la persona: ")
        edadn = input("Edad: ")
        telefonon = input("Telefono: ")
        RegistrarNpersona()
        print("Bien el usuario ha sido registrado")
        print("------------------------------")

    elif opcion == "2":
        print("---------------------------------")
        print("->Los usuarios registrados son: <-")
        print(P.mostrarPer())
        print("---------------------------------")
    
    
    elif opcion == "3":
        print("->Crear Articulos<-")
        nmaterial = input("Porfavor coloca el nombre del articulo: ")
        RegistrarNMaterial()
        print("Articulo registrado!!!")
    
    elif opcion == "4":
        print("->Ver Material<-")
        print(m.verMateriales())
    
    elif opcion == "5":
        print("->PEDIDOS<-")
        usu = input("Nombre del usuario: ")
        materia = input("Que material es que elegiste: ")
        can = input("Cantidad: ")
        print("Bien hecho el prestamo fue echo correctamente")
        RegistraNPrestamo(usu,materia,can)

    elif opcion == "6":
        print("->Entregar Material<-")
        folios = int(input("Numero de folio porfavor: "))
        RegistrarNDevoluciones(folios)

    elif opcion == "7":
        print("->INFORMACION<-")
        print(Prestamos.VerPrestamos())
    
    elif opcion == "8":
        print("Hasta luego....")
        pop = False
    
    else:
        print("Opcion no existente vuelve a checar otras opciones")
    