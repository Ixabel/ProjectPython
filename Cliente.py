class Cliente:
    'Clase que maneja los datos de un Cliente'

    def __init__(self, nombre="", direccion="",telefono="", email=""):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email

    def setNombre(self, nombr):
        self.nombre = nombr

    def setDireccion(self, dir):
        self.direccion =dir

    def setTelefono(self, tno):
        self.telefono =tno

    def setEmail(self,correo):
       self.email=correo

    def getNombre(self):
        return(self.nombre)

    def getDireccion(self):
        return(self.direccion)

    def getTelefono(self):
        return(self.telefono)

    def getEmail(self):
        return(self.email)