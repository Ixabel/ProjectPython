#Definicion de CLASE Persona
class Persona:
    'Clase que maneja los datos de un Persona'

    def __init__(self, nombre="", direccion=""):
        self.nombre=nombre
        self.direccion=direccion


    def setNombre(self, nomb):
        self.nombre = nomb

    def setDireccion(self, dir):
        self.direccion = dir

    def getNombre(self):
        return(self.nombre)

    def getDireccion(self):
        return(self.direccion)

class Empleado(Persona):

    def __init__(self, nombre="", direccion="", cargo="", sueldo=0):
        super().__init__(nombre,direccion)
        self.cargo=cargo
        self.sueldo=sueldo

    def setCargo(self, cargo):
        self.cargo = cargo

    def setSueldo(self, sueldo):
        self.sueldo = sueldo

    def getCargo(self):
        return(self.cargo)

    def getSueldo(self):
        return(self.sueldo)

class Jefe(Empleado):
    def __init__(self, departamento=""):
        super().__init__()
        self.departamento = departamento

    def setDepartamento(self,departamento):
        self.departamento=departamento

    def getDepartamento(self):
        return(self.departamento)



P1=Persona("Paco")
reme=Persona()

ivan=Empleado('Ivan', 'Bilbao','Técnico',1200)
print(ivan.nombre + '-' + ivan.direccion + '-' + ivan.cargo + '-',ivan.sueldo)

jefe=Jefe('Departamento de Ventas')
print(jefe.nombre + '-' + jefe.direccion + '-' + jefe.cargo + '-',jefe.sueldo, '-',jefe.departamento)
jefe.setNombre('Isabel')
jefe.setCargo('Responsable')
jefe.setDireccion('Donosti')
jefe.setSueldo(2500)
print(jefe.nombre + '-' + jefe.direccion + '-' + jefe.cargo + '-',jefe.sueldo, '-',jefe.departamento)