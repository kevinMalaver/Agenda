import json
from contacto import Contacto
from util import Util 
import os
class Agenda:

    lista_contactos = []

    def __init__(self):
        pass
    
    def agregar_contactos(self, contactos_nuevos: list[Contacto]) -> None:
        with open("contactos.json", "w") as archivo:
            json.dump(Util.objetos_a_diccionarios(contactos_nuevos), archivo, indent=4)
    
    def obtener_contactos(self) -> None:
        if os.path.exists("contactos.json"):
            with open("contactos.json", "r") as archivo:
                contactos = json.load(archivo)
            self.lista_contactos = Util.diccionarios_a_objetos(contactos)
    
    def buscar_contacto(self, id: int = -1, nombre: str = "") -> Contacto:
        if len(self.lista_contactos) == 0:
            self.obtener_contactos() 
        for contacto in self.lista_contactos:
            if contacto.id == id or contacto.nombre == nombre:
                return contacto
        return None
    
    def eliminar_contacto(self, id: int) -> None:
        if len(self.lista_contactos) == 0:
            self.obtener_contactos() 
        for contacto in self.lista_contactos:
            if contacto.id == id:
                self.lista_contactos.remove(contacto)
                break
        with open("contactos.json", "w") as archivo:
            json.dump(Util.objetos_a_diccionarios(self.lista_contactos), archivo, indent=4)

if __name__ == "__main__":
    lista_contactos = [
        Contacto("Kevin", 3102338255, "kevinmalaver3@gmail.com"),
        Contacto("Brayan", 3115150880, "brayancobos741@gmail.com"),
        Contacto("Emilce", 3223366143, "emicoar@gmail.com")]
    #Prueba de la clase Agenda
    agenda = Agenda()
    agenda.agregar_contactos(lista_contactos)
    agenda.obtener_contactos()
    agenda.eliminar_contacto(2)
    for contacto in agenda.lista_contactos:
        print(contacto.id, contacto.nombre, contacto.telefono, contacto.correo)
    print(agenda.buscar_contacto(1).correo)



