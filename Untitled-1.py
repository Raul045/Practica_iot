import clase_material
import Clase_Accion
import Clase_Persona
menu = """
|||---->Bievenido al centro deportivo<----||||
°A continuacion te mostraremos las opciones disponibles°
------->Menu<------
1.- Agregar usuario
2.- Informacion del sistema
3.- Entregar material
4.- Recibir material
5.- Informacion de Pendientes
6.- Salir 
"""
pop = True
while pop == True:
    print(menu)
    opcion = input("Elige la opcion que gustes: ")
    
    if opcion == "1":
        print("------------------------------")
        print("->Agregar Usuario<-")
        Clase_Accion.Registrar()
        print("Bien el usuario ha sido registrado")
        print("------------------------------")

    elif opcion == "2":
        print("---------------------------------")
        print("->Los usuarios registrados son: <-")
        print(Clase_Accion.Mostrar())
        print("---------------------------------")
    
    elif opcion == "3":
        print("->PEDIDOS<-")
        Clase_Accion.Pedir()
    
    elif opcion == "4":
        print("->Entregar material<-")
        Clase_Accion.Entregar()

    elif opcion == "5":
        print("->informacion<-")
        Clase_Accion.Minfo()

    elif opcion == "6":
        print("Hasta luego....")
        pop = False
    
    else:
        print("Opcion no existente vuelve a checar otras opciones")
    