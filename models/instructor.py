# Modelo Instructor
import bcrypt
from mongoengine import StringField, ReferenceField, Document
from models.regional import Sena

class Instructor(Document):
    nombrecompleto = StringField(required=True)
    correoelectronico = StringField(required=True, unique=True)
    regional = ReferenceField(Sena, required=True)
    contrasena = StringField(required=True)

    def __str__(self):
        return self.nombrecompleto

    # Método para cifrar la contraseña antes de guardarla
    def set_password(self, password):
        self.contrasena = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Método para verificar la contraseña ingresada durante el login
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.contrasena.encode('utf-8'))
