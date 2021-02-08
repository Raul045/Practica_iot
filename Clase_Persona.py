# from pymongo import MongoClient

# Mongo_URI = 'mongodb://localhost'

# cliente = MongoClient(Mongo_URI)
# db = cliente['CentroDeportivo']
# collection = db['Personas']

import json

class Persona():
  matricula = 0         
  registro = 0    
  Lista = []
  data = {}
  data['Lista'] = []

  def __init__(self, matri=None, nombre=None, edad=None, telefono=None, p=None):
      self.matri = matri
      self.nombre=nombre
      self.edad=edad
      self.telefono=telefono
      p = 1
    
  def Registro(self,nombres,edadn,telefonon):
      self.matricula += 1
      newPerson = Persona(self.matricula,nombres,edadn,telefonon)
      self.Lista.append(newPerson)
      self.data['Lista'].append(reconPersonas(newPerson))
      with open('Personas.json','w') as p:
          json.dump(self.data, p, indent=4)
    #   collection.insert_one({self.data})

  def mostrarPer(self):
      leer = json.loads(open('Personas.json').read())
      print(leer)

  def Disponibles(self, miembro, prestamosDis):
      for mi in self.Lista:
          if miembro == mi.matricula:
              mi.p += prestamosDis
          return True
      return False


def reconPersonas(persona):
    if isinstance(persona,Persona):
        return{
            'id'  : persona.matri,
            'nombre' : persona.nombre,
            'edad' : persona.edad,
            'telefono' : persona.telefono
        }
    raise TypeError(f'El objeto de {persona} no es del mismo tipo')



        