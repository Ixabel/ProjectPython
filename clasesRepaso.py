class Vehiculo:
    def __init__(self,nombre='', matricula='', marca='', modelo='', numRuedas=0, caballos=''):
        self.nombre = nombre
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.numRuedas = numRuedas
        self.caballos = caballos

    def setNombre(self, nombre):
        self.nombre = nombre

    def setMatricula(self, matricula):
        self.matricula = matricula

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo =modelo

    def setNumRuedas(self, numRuedas):
        self.numRuedas = numRuedas

    def setCaballos(self, caballos):
        self.caballos = caballos

    def getNombre(self):
        return (self.nombre)

    def getMatricula(self):
        return(self.matricula)

    def getMarca(self):
        return(self.marca)

    def getModelo(self):
        return (self.modelo)

    def getNumRuedas(self):
        return (self.numRuedas)

    def _str_(self):
        cadena=""
        cadena=self.nombre
        cadena=cadena+'-'
        cadena+=self.matricula
        cadena = cadena + '-'
        cadena+=self.marca
        cadena = cadena + '-'
        cadena+=self.modelo
        cadena = cadena + '-'
        cadena+=str(self.numRuedas)
        return(cadena)

    def getCaballos(self):
        return (self.caballos)

class Moto(Vehiculo):
    def __init__(self, nombre='', matricula='', marca='', modelo='', numRuedas=2, caballos='',chuches=[]):
       super().__init__(nombre, matricula, marca,modelo,numRuedas)
       self.chuches=[chuches]

    def setChuches(self, chuches):
        self.chuches = [chuches]

    def getChuches(self):
        return (self.chuches)

    def addChuche(self,chuche):
        self.chuches.append(chuche)

    def quitarChuche(self,chuches,i):
        del(chuches[i])

class Coche(Vehiculo):
    def __init__(self, nombre='', matricula='', marca='', modelo='', numRuedas=4, caballos=''):
       super().__init__(nombre, matricula, marca,modelo,numRuedas)



V1=Vehiculo("Pepito","5555PLN","Volkswagen","5",4)
print(V1._str_())

V1=Vehiculo("Cacito","4458JJJ","BMW","5",4)
print(V1._str_())

M1=Moto("KKKK","1111KKK","GP","X",2,'Gominola')
print(M1._str_()+'-',M1.chuches)
M1.addChuche('Piruleta')
print(str(M1.chuches))
M1.quitarChuche(M1.chuches,0)
print(str(M1.chuches))

#listadoChuches=[]
#listadoChuches.append('Gominola')
#for i in listadoChuches:
 #   print(i)

