#Definicion de CLASE Cliente
class Cliente:
    'Clase que maneja los datos de un Cliente'
    numIncrementoCotizaciones=0

    def __init__(self, nombre="", direccion="",telefono="", email="",cotizacion=0,totalCotizacion=0):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email
        self.cotizacion=cotizacion
        self.totalCotizaciones=totalCotizacion

    def setNombre(self, nombr):
        self.nombre = nombr

    def setDireccion(self, dir):
        self.direccion =dir

    def setTelefono(self, tno):
        self.telefono =tno

    def setEmail(self,correo):
       self.email=correo

    def setCotizacion(self,cotiz):
        self.cotizacion = cotiz
        self.totalCotizaciones=self.totalCotizaciones+cotiz
        Cliente.numIncrementoCotizaciones+=1

    def getNombre(self):
        return(self.nombre)

    def getDireccion(self):
        return(self.direccion)

    def getTelefono(self):
        return(self.telefono)

    def getEmail(self):
        return(self.email)

    def getCotizacion(self):
        return(self.cotizacion)

    def getTotalCotizaciones(self):
        return(self.totalCotizaciones)


indra=Cliente()
indra.nombre="Isabel"
indra.direccion="Vitoria"
indra.telefono="666666666"
indra.email="larrinoa@gmail.com"
indra.cotizacion=4000
indra.setCotizacion(2000)

print(indra.nombre + '-' + indra.direccion + '-' + indra.telefono + '-' + indra.email + '-' ,indra.cotizacion)
print(indra.cotizacion)
print(indra.getCotizacion())

#*****************VARIOS CLIENTES***********************************************
C1=Cliente("Pepe")
print(C1.nombre + '-' + C1.direccion + '-' + C1.telefono + '-' + C1.email + '-',C1.cotizacion)
C1=Cliente(direccion="Bilbao")
print(C1.nombre + '-' + C1.direccion + '-' + C1.telefono + '-' + C1.email + '-',C1.cotizacion)
C1=Cliente("Pepe", direccion="Bilbao")
print(C1.nombre + '-' + C1.direccion + '-' + C1.telefono + '-' + C1.email + '-',C1.cotizacion)


C1.setNombre("Pepe")
C1.setDireccion("Bilbao")
C1.setTelefono("9999")
C1.setEmail("@@@")
C1.setCotizacion(50000)
C1.setCotizacion(50005)
print(C1.nombre + '-' + C1.direccion + '-' + C1.telefono + '-' + C1.email + '-' + str(C1.cotizacion) + '-' +str(C1.totalCotizaciones))
print(C1.nombre + '-' + C1.direccion + '-' + C1.telefono + '-' + C1.email + '-' + str(C1.cotizacion) + '-', C1.getTotalCotizaciones(),C1.numIncrementoCotizaciones)
#*******************************************************************************