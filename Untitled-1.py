#---------------------------MongoDB------------------------..................#
from pymongo import MongoClient

Mongo_URI = 'mongodb://localhost'

cliente = MongoClient(Mongo_URI)

db = cliente['CentroDeportivo']
#-------------------------------mysql--------------------------------------#
import mysql.connector
dbs = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'centro_depo'
)

import datetime


from clase_material import Material as material

from Clase_Persona import Persona 

from Clase_Accion import Prestamo as pre


m = material()
P = Persona()
Prestamos = pre()

def RegistrarNpersona():
    person = P.Registro(nombres,edadn,telefonon)
    mycursor = dbs.cursor()
    con = "INSERT INTO personas (Nombre, Edad, Telefono) VALUES (%s, %s, %s)"
    val = (nombres, edadn, telefonon)
    mycursor.execute(con, val)
    dbs.commit() 
    

def RegistrarNMaterial():
    mat = m.RegistroArticulo(nmaterial,Exist)
    print("Material Registrado: " + mat.articulo)
    mycursor1 = dbs.cursor()
    con1 = "INSERT INTO material (NMaterial, Cantidad) VALUES (%s, %s)"
    val1 = (nmaterial, Exist)
    mycursor1.execute(con1, val1)
    dbs.commit()

def RegistraNPrestamo(usu, materia, can):
    datosValidados = (usu,materia,can)
    fecha = str(datetime.datetime.now())
    prestamo = Prestamos.RegistroPrestamo(usu, materia, can, fecha)
    collection = db['Prestamos']
    collection.insert_one({"Usuario": usu, "Material": materia, "Cantidad": can, "Fecha": fecha})
    #--------------------------------------------------------#
    mycursor2 = dbs.cursor()
    con2 = "INSERT INTO prestamos (Usuario, MaterialP, Cantidad, fecha) VALUES (%s, %s, %s, %s)"
    val2 = (usu, materia, can, fecha)
    mycursor2.execute(con2, val2)
    dbs.commit()
    #____________________________________________________#
    print("Su folio es: " +  str(prestamo.folio))

def RegistrarNDevoluciones(folios):
    devolucion = Prestamos.RegistroDevolucion(folios)
    # print("Devolucion Exitosa")
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
        collection = db['Personas']
        collection.insert_one({"Nombre": nombres, "Edad": edadn, "Telefono": telefonon})

    elif opcion == "2":
        print("---------------------------------")
        print("->Los usuarios registrados son: <-")
        print(P.mostrarPer())
        print("---------------------------------")
    
    
    elif opcion == "3":
        print("->Crear Articulos<-")
        nmaterial = input("Porfavor coloca el nombre del articulo: ")
        Exist = input("Cantidad de Existencias: ")
        RegistrarNMaterial()
        print("Articulo registrado!!!")
        print("------------------------")
        collection = db['Material']
        collection.insert_one({"NMaterial": nmaterial, "Existencia": Exist})
    
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
        # folios = input("Nombre porfavor: ")
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
    