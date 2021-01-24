import json

class Material():
  registro = 0
  Material = []
  data = {}
  data['Material'] = []

  def __init__(self,regist =None ,articulo=None):
    self.regist = regist
    self.articulo  = articulo

  def RegistroArticulo(self, articulo):
    self.registro += 1
    newMaterial = Material(articulo)
    self.Material.append(newMaterial)
    self.data['Material'].append(reconMateriales(newMaterial))
    with open('Materiales.json', 'w') as M:
      json.dump(self.data, M, indent=4)
    return newMaterial
  
  def verMateriales(self):
       leerm = json.loads(open('Materiales.json').read())
       print(leerm)

  def ValidarDatosArticulo(self, mater,canti):
    for a in self.ListaArticulos:
      if mater == a.Id:
        if a.inventario > 0:
          if cantidad <= a.inventario:
            return True
          else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del articulo")
        else: print("| Prestamo Rechazado|Articulo solicitado agotado")
        break
    else: print("| Prestamo Rechazado|El articulo solicitado no existe")
  

def reconMateriales(material):
  if isinstance(material,Material):
    return {
      'ID'         : material.regist,
      'Material'   : material.articulo
    }
  raise TypeError(f'El objeto {material} no es de tipo Persona')