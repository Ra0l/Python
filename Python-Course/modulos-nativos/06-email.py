from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = """ 
    <b>Hola Mundo! $usuario</b>
"""
template = Template(plantilla)
cuerpo = template.substitute()

path = Path("Python-Course/modulos-nativos/heart-red.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "ultimatepython@.com.pe"
mensaje["subject"] = "Esto es una prueba"
cuerpo = MIMEText("CUERPO DEL MENSAJE")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp-relay.gmail.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login("raul.aliaga.dev@gmail.com", "T3csup3922")
    smpt.send_message(mensaje)
    print("Mensaje enviado")
