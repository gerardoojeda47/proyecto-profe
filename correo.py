import threading
import yagmail

def enviar_correo_asincrono(correo_destino, asunto, mensaje):
    def enviar():
        try:
            yag = yagmail.SMTP("gerardozapatos@gmail.com","ktyvkqnowaoytjnm'", encoding="utf-8")
            yag.send(to=correo_destino, subject=asunto, contents=mensaje.encode('utf-8').decode('utf-8'))
            print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
    
    hilo = threading.Thread(target=enviar)
    hilo.start()