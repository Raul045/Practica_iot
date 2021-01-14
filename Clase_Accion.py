from Clase_Persona import *
datos = []
from clase_material import *
m = []

def Registrar():
    nombre = input("Nombre de la persona: ")
    edad = input("Edad: ")
    telefono = input("Telefono: ")

    usuario = Persona(nombre, edad, telefono)
    datos.append(usuario)

def Mostrar():
    for usuario in datos:
        print("Nombre: " + usuario.nombre + "\nEdad: " + usuario.edad + "\n")

def Pedir():
    nombre = input("Porfavor coloca tu nombre: ")
    Nmaterial = input("Nombre del material: ")
    cantidad = input("Cantidad que necesitas: ")
    fechaPe = input("Fecha de Pedido: ")

    for usuario in datos:
        if usuario.nombre == nombre or usuario.bolsa > "0":
            usuario.nombreMaterial = Nmaterial
            usuario.cantidad = cantidad
            usuario.fechaP = fechaPe
            usuario.bolsa = cantidad
            print("Bien el pedido fue agregado exitosamente :)")
            break
        else:
            print("Lo sentimos pero esa persona no existe en el sistema")
            print("Advertencia por seguridad de la empresa solo puedes tomar un pedido hasta no haber devuelto el anterio no puedes pedir otro :(")
            
def Entregar():
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    fechaD = input("Fecha de entrega: ")

    for usuario in datos:
        if usuario.nombre == nombre:
            usuario.cantidad = cantidad
            usuario.fechaD = fechaD
            if fechaD != "":
                usuario.cantidad = "0"
                usuario.fechaP = ""
                usuario.fechaD = ""
                usuario.bolsa = "0" 
                print("Bien los productos fueron entregados")
def Minfo():
    p=[]
    for canasta in datos:
        if canasta.bolsa > "0":
            p.append(canasta)
        else:
            print("sin deudas")
    
    for canasta in p:
        if canasta == 0:
            print("no debes nada UUUUUUUHHH")
        else:
            print("Pedidos")
            print("Nombre: " + canasta.nombre + "\nMaterial: " + canasta.nombreMaterial + "\nFecha de pedido: " + canasta.fechaP + "\n")
        
    

    