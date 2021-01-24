import json

class Persona:             
    Lista = []
    data = {}
    data['Lista'] = []

    def __init__(self, nombre=None, edad=None, telefono=None):
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
    
    def Registro(self,nombres,edadn,telefonon):
        newPerson = Persona(nombres,edadn,telefonon)
        self.Lista.append(newPerson)
        self.data['Lista'].append(reconPersonas(newPerson))
        with open('Personas.json','w') as p:
            json.dump(self.data, p, indent=4)
    

    def mostrarPer(self):
        leer = json.loads(open('Personas.json').read())
        print(leer)

def reconPersonas(persona):
    if isinstance(persona,Persona):
        return{
            'nombre' : persona.nombre,
            'edad' : persona.edad,
            'telefono' : persona.telefono
        }
    raise TypeError(f'El objeto de {persona} no es del mismo tipo')



        