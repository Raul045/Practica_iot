import json
import datetime

from Clase_Persona import Persona as p
from clase_material import Material as m

P=p()
M=m()

class Prestamo:
    regis = 0
    Prestamos = []
    data = {}
    data['Prestamos'] = []

    def __init__(self, folio=None , Usuario=None, material=None, cantidad=None, fPrestamo=None, devuelto=None, fDevolucion=None):
        self.folio  = folio
        self.Usuario = Usuario
        self.material = material
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        self.devuelto       = False
        self.fDevolucion    = ""

    def RegistroPrestamo(self, usuarion, materialn, cantidadn, fechan):
        self.regis += 1
        newPrestamo = Prestamo(self.regis, usuarion, materialn, cantidadn, fechan)
        self.Prestamos.append(newPrestamo)
        self.data['Prestamos'].append(reconPrestamos(newPrestamo))
        with open('Prestamos.json', 'w') as Pre:
            json.dump(self.data, Pre, indent=4)
        for k in self.Prestamos:
            if self.regis == k.folio:
                return(newPrestamo)

    def RegistroDevolucion(self, folio):
        i = 0
        for j in self.Prestamos:
            if folio == j.folio:
                fechaD = str(datetime.datetime.now())
                j.devuelto = True
                j.fDevolucion = fechaD
                Usuario = j.Usuario
                material = j.material
                cantidad = j.cantidad
                disponibles = P.Disponibles(Usuario, 1)
                if disponibles:
                    disponibles = m.Bodega(material, cantidad)
                    return True
        return False
                
    
    def VerPrestamos(self):
        leerp = json.loads(open('Prestamos.json').read())
        print(leerp)

          
       


def reconPrestamos(prestamo):
  if isinstance(prestamo,Prestamo):
    return {
      'folio'        : prestamo.folio,
      'Nombre'       : prestamo.Usuario,
      'material'     : prestamo.material,
      'cantidad'     : prestamo.cantidad,
      'fPrestamo'    : prestamo.fPrestamo,
      'devuelto'     : prestamo.devuelto,
      'fDevolucion'  : prestamo.fDevolucion
    }
  raise TypeError(f'El objeto {prestamo} no es de tipo Persona')