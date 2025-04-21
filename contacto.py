class Contacto:
    ID = 0
    def __init__(self, nombre, telefono, correo,  id = None):
        if id is None:
            Contacto.ID += 1
            self.id = Contacto.ID
        else:
            self.id = id
            Contacto.ID = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
   
