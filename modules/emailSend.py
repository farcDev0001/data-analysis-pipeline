import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getEnv import getVariable

def sendEmail(pathPdf):
    
    subject = "Informe adjunto en el Email"
    body = "Report in pdf"
    sender_email = getVariable('email')[0]
    receiver_email = input('Insert the receiver email: ')
    password = getVariable('password')[0]
    
    # Cabecera del email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Cuerpo del email
    message.attach(MIMEText(body, "plain"))

    filename = pathPdf # el nombre va a ser el mismo que el del pdf

    # Abro el pdf
    with open(filename, "rb") as attachment:
    
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Codificación en ASCII     
    encoders.encode_base64(part)

    # Añado la cabecera
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Se agrega el archivo adjunto
    message.attach(part)
    text = message.as_string()

    # Login usando protocolo seguro ssl y envío del mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

