import json

class Material():
  Material = []
  data = {}
  data['Material'] = []

  def __init__(self, articulo=None):
    self.articulo       = articulo

  def RegistroArticulo(self, articulo):
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
  
  def CantidadInventario(self, articulo, cantidad):
    for a in self.ListaArticulos:
      if articulo == a.Id:
        a.inventario += cantidad
        return True
      break

def reconMateriales(material):
  if isinstance(material,Material):
    return {
      'Material'   : material.articulo
    }
  raise TypeError(f'El objeto {material} no es de tipo Persona')