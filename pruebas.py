# import mysql.connector
# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'pruebas_python'
# )

# mycursor = db.cursor()

# con = "INSERT INTO personas (id, Nombre) VALUES (%s, %s)"
# val = (1, "Raul")
# mycursor.execute(con, val)

# db.commit()




# from pymongo import MongoClient

# Mongo_Uri = 'mongodb://localhost'

# cliente = MongoClient(Mongo_Uri)

# db = cliente['Centro_Deportivo']
# collection = db['Deportes']

# persona1 = {"ID": 1, "Nombre": "Alejandro"}

# persona2 = {"ID": 2, "Nombre": "Oscar"}

# collection.insert_many([persona1, persona2])


# archivo.write("holaaaaaaaaaaa")
# n = int(input("Di cuantas veces deseas registrar nombres: "))
# personas =[{
#   "Nombre": "",
#   "edad": "",
#   "telefono": ""
# }]
# menu="""
# --------Menu-----------
# 1.- Registrar Usuario |
# 2.- Mostrar           |
# 3.- Salir             |
# -----------------------
# """
# pop = True
# while pop == True:
#     archivo = open("laspruebas.txt","a")
#     print(menu)
#     opcion = input("Que deseas hacer: ")

#     if opcion == "1":
#         nombre = input("coloca el nombre porfavor: ")
#         edad = input("Coloca tu edad: ")
#         telefono = input("Coloca tu telefono: ")
#         personas.update({"Nombre":nombre,"edad":edad,"telefono":telefono})
#         archivo.write('personas=%s'%personas)
    
#     elif opcion == "2":
#         f = open("laspruebas.txt", "r")
#         print(f.readline())
    
#     elif opcion == "3":
#         print("Hasta luego....")
#         pop = False

#     else:
#         print("no vale esa opcion :(")

# archivo.close()
