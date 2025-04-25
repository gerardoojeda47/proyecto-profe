from flask import request, render_template, jsonify, redirect, url_for, session, flash
from models.instructor import Instructor
from models.regional import Sena
from app import app  
import bcrypt
import random
import string
import yagmail
import threading







# Función para generar una contraseña aleatoria
def generar_contrasena(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))


def enviar_correo_asincrono(correo_destino, asunto, mensaje):
    def enviar():
        try:
            yag = yagmail.SMTP("santiagoquilindo32@gmail.com", "devoxgkdtzkduepy", encoding="utf-8")
            yag.send(to=correo_destino, subject=asunto, contents=mensaje.encode('utf-8').decode('utf-8'))
            print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
    hilo = threading.Thread(target=enviar)
    hilo.start()


@app.route("/agregarintructor/", methods=['GET', 'POST'])
def addInstructor():
    try:
        mensaje = None
        estado = False
        if request.method == 'POST':
            datos = request.get_json()
            print("Datos recibidos:", datos)
            sena_id = datos.get('sena_id')
            print("Sena ID recibido:", sena_id)

            if not sena_id:
                raise ValueError("No se recibió el 'sena_id'.")

            # Buscar la región (Sena) asociada
            sena = Sena.objects(id=sena_id).first()
            print("Sena encontrado:", sena)

            if not sena:
                raise ValueError("El Sena seleccionado no existe.")

            datos['regional'] = sena
            datos['correoelectronico'] = datos.get('email')
            del datos['email']
            del datos['sena_id']

            # Si no se proporciona una contraseña, generar una contraseña aleatoria
            if 'contrasena' not in datos:
                datos['contrasena'] = generar_contrasena()  # Generar contraseña aleatoria si no existe

            # Cifrar la contraseña antes de almacenarla
            instructor = Instructor(**datos)
            instructor.set_password(datos['contrasena'])  # Asegúrate de cifrar la contraseña
            instructor.save()

            # Enviar la contraseña al correo del instructor
            correo_destino = datos['correoelectronico']
            asunto = "Contraseña generada para acceder"
            mensaje = f" {datos['contrasena']}"
            enviar_correo_asincrono(correo_destino, asunto, mensaje)
            estado = True
            mensaje = "Correo enviado"
        else:
            mensaje = "Método no permitido"
    except Exception as error:
        print("Error al agregar instructor:", error)
        mensaje = str(error)

    # Obtener todas las regiones (Sena)
    senas = Sena.objects()
    return render_template('agregar_instructor.html', estado=estado, mensaje=mensaje, senas=senas)



@app.route("/login", methods=['GET', 'POST'])
def login():
    mensaje = None
    estado = False
    if request.method == 'POST':
        correo = request.form.get('email')
        password = request.form.get('password')

        # Buscar al instructor por correo
        instructor = Instructor.objects(correoelectronico=correo).first()

        # Verificar que el instructor exista y la contraseña sea correcta
        if instructor:
            print(f"Usuario encontrado: {instructor.nombrecompleto}")  # Depuración

            if instructor.check_password(password):  # Usamos el método check_password del modelo Instructor
                session['usuario_id'] = str(instructor.id)  # Guardar el ID del usuario en la sesión
                estado = True
                flash("Login exitoso", "success")
                return redirect(url_for('index'))  # Redirigir a la página del Dashboard o la que desees
            else:
                flash("Credenciales incorrectas", "danger")  # Mensaje si las credenciales no son correctas
        else:
            flash("Credenciales incorrectas", "danger")  # Si no se encuentra el instructor

    return render_template('login.html', estado=estado, mensaje=mensaje)



#cerrar sesión
@app.route('/logout')
def logout():
    session.pop('instructor_id', None)
    flash('¡Has cerrado sesión!', 'info')
    return redirect(url_for('login'))