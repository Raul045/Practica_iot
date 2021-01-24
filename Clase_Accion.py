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
        newPrestamo = Prestamo(usuarion, materialn, cantidadn, fechan)
        self.Prestamos.append(newPrestamo)
        self.data['Prestamos'].append(reconPrestamos(newPrestamo))
        with open('Prestamos.json', 'w') as Pre:
            json.dump(self.data, Pre, indent=4)
        for k in self.Prestamos:
            if self.regis == k.folio:
                return(newPrestamo)

    def RegistroDevolucion(self, folion):
        i = 0
        for j in self.Prestamos:
            if folion == j.folio:
                fechaD = str(datetime.datetime.now())
                r.devuelto = True
                r.fDevolucion = fechaD
                usuario = j.usuario
                material = j.material
                cantidad = j.cantidad
                disponibles = p.PrestamosDisponibles(usuario, 1)
                if disponibles:
                    disponibles = a.CantidadInventario(material, cantidad)
                    return True
        return False
                
    
    def VerPrestamos(self):
        leerp = json.loads(open('Prestamos.json').read())
        print(leerp)

    def ValidarDatosPrestamo(self, usua,mar,cant):
        #Validar que haya usuarios y tengan prestamos disponibles
        pase = p.ValidarDatosPersona(usua)
        if pase:
            pase =a.ValidarDatosArticulo(mar,cant)
            if pase:
                disponibles = p.PrestamosDisponibles(miembro, -1)
                if disponibles:
                    disponibles = a.CantidadInventario(articulo, -cantidad)
                    return True
        else: False
          
        # for m in P.ListaMiembros:
        #     if miembro == m.Id:
        #         if m.prestamos > 0:
        #             #Validar que haya articulos y cantidad requerida
        #             for ar in A.ListaArticulos:
        #                 if articulo == ar.Id:
        #                     if ar.inventario > 0:
        #                         if cantidad <= ar.inventario:
        #                             return True
        #                         else: print("| Prestamo Rechazado|No se tiene la cantidad suficiente del ariticulo")
        #                         break
        #                     else: print("| Prestamo Rechazado|Articulo solicitado agotado")
        #                     break
        #             else: print("| Prestamo Rechazado|El articulo solicitado no existe")
        #             break
        #         else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
        #         break
        #     else: print("| Prestamo Rechazado|Miembro no registrado")
        # return False



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