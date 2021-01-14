class Material():
    materiaP = ""
    cantidad = 0
    fechaP = ""
    fechaD = "0"
    nombrem = "Balon de futbol"
    def __init__(self, nombrem):
        self.nombrem = nombrem
    
    def __str__(self):
        return "Material: " + self.nombrem 

