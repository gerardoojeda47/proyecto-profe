# from flask import request, render_template, redirect, url_for, flash, session
# from flask_mail import Message, Mail
# from models.instructor import Instructor
# from app import app, mail
# import bcrypt
# from dotenv import load_dotenv
# import os

# load_dotenv()

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     mensaje = None
#     estado = False
#     if request.method == 'POST':
#         correo = request.form.get('email')
#         password = request.form.get('password')

#         # Buscar al instructor por correo
#         instructor = Instructor.objects(correoelectronico=correo).first()

#         # Verificar que el instructor exista y la contraseña sea correcta
#         if instructor and instructor.check_password(password):  # Usamos el método check_password del modelo Instructor
#             session['usuario_id'] = str(instructor.id)  # Guardar el ID del usuario en la sesión
#             estado = True
#             flash("Login exitoso", "success")
#             return redirect(url_for('index'))  # Redirigir a la página del Dashboard o la que desees
#         else:
#             flash("Credenciales incorrectas", "danger")  # Mensaje si las credenciales no son correctas

#     return render_template('login.html', estado=estado, mensaje=mensaje)
