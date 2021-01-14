class Persona():
    materiaP = ""
    cantidad = 0
    fechaP = ""
    fechaD = ""
    bolsa = "" 
    nombreMaterial = ""
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
    
    def __str__(self):
        return "Usuario: " + self.nombre + "\nEdad: " + self.edad + "\nTelefono: " + self.telefono
    
        