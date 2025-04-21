from contacto import Contacto
class Util():
    @staticmethod
    def objetos_a_diccionarios(contactos: list[Contacto])-> list[dict]:
        return [{"id" : contacto.id, "nombre" : contacto.nombre, "telefono" : contacto.telefono, "correo" : contacto.correo} for contacto in contactos]
    
    @staticmethod
    def diccionarios_a_objetos(contactos: list[dict])-> list[Contacto]:
        return [Contacto(contacto["nombre"], contacto["telefono"], contacto["correo"], contacto["id"]) for contacto in contactos ]