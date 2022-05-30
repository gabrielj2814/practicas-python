class VTuber():
    
    def __init__(self):
        self.__nombre=""
        self.__plataforma=""
    
    def setNombre(self,nombre_):
        self.__nombre=nombre_

    def getNombre(self):
        return self.__nombre

    def setPlataforma(self,plataforma_):
        self.__plataforma=plataforma_

    def getPlataforma(self):
        return self.__plataforma

continuar="y"
listaVTubers=[]
while(continuar=="y"):
    nombreVTuber=input("ingresar nombre del VTuber: ")
    nombrePlataforma=input("aingresar plataforma en donde hace Stream: ")
    vtuber=VTuber()
    vtuber.setNombre(nombreVTuber)
    vtuber.setPlataforma(nombrePlataforma)
    listaVTubers.append(vtuber)
    continuar=input("desea continuar agregando vtubers y\n: ")

for vtuber in listaVTubers:
    print(vtuber.getNombre()+" y hace stream en  "+vtuber.getPlataforma())