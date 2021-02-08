import json

class Material():
  registro = 0
  Materiales = []
  data = {}
  data['Materiales'] = []

  def __init__(self, regist=None, articulo=None, existencia = None):
    self.regist = regist
    self.articulo  = articulo
    self.existencia = existencia

  def RegistroArticulo(self, articulo, existencia):
    self.registro += 1
    newMaterial = Material(self.registro,articulo, existencia)
    self.Materiales.append(newMaterial)
    self.data['Materiales'].append(reconMateriales(newMaterial))
    with open('Materiales.json', 'w') as M:
      json.dump(self.data, M, indent=4)
    return newMaterial
  
  def verMateriales(self):
       leerm = json.loads(open('Materiales.json').read())
       print(leerm)

  def ValidarDatosArticulo(self, mater,canti):
    for a in self.Materiales:
      if mater == a.regist:
        if a.existencia > 0:
          if cantidad <= a.existencia:
            return True
          else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del articulo")
        else: print("| Prestamo Rechazado|Articulo solicitado agotado")
        break
    else: print("| Prestamo Rechazado|El articulo solicitado no existe")


  def Bodega(self, material, cantidad):
    for b in self.Materiales:
      if material == b.regist:
        b.existencia += cantidad
        return True
      break
  

def reconMateriales(material):
  if isinstance(material,Material):
    return {
      'ID'         : material.regist,
      'Material'   : material.articulo
    }
  raise TypeError(f'El objeto {material} no es de tipo Persona')