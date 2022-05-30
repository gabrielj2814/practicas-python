class YouTuber():
    
    def __init__(self,nombre_,correo_):
        self.__nombre=nombre_
        self.__correo=correo_
        self.__nombre_comunidad=""

    def getDatos(self):
        # agregando un f al lado de un string se puede 
        # hacer interpolacion dentron del string con {vinculacion\variable}
        print(f"nombre: {self.__nombre} \ncorreo: {self.__correo}")


class VTuber(YouTuber):
    
    def __init__(self, nombre_, correo_,tipoVTuber_):
        super().__init__(nombre_, correo_)
        self.tipoVTuber=tipoVTuber_
    
    def getDatos(self):
        super().getDatos()
        print(f"tipo de VTuber: {self.tipoVTuber}")


vtuber=VTuber("Rakkun","rakkun@gmail.com","2D")
youTuber=YouTuber("rubius","rubius@gmail.com")

vtuber.getDatos()
youTuber.getDatos()