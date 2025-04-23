from mongoengine import Document, StringField, ReferenceField
from models.instructor import Instructor

class NombreGuia(Document):
    nombreguia = StringField(max_length=80, required=True)
    descripcions = StringField(max_length=80, required=True)
    programaformacion = StringField(max_length=80, required=True)
    documento = StringField(max_length=200, required=True) 
    fecha = StringField(max_length=80, required=True)
    intructordeproceso = ReferenceField(Instructor, required=True)

    def __repr__(self):
        return self.nombreguia