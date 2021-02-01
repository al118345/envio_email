import smtplib
from envio_email.password import password_gmail

'''
Clase que tiene como objetivo enviar email.
'''
class SendEMail():
    def send_email_test(self, para):

        #dirección desde dónde se envian los correos
        gmail_user = '1938web@gmail.com'
        gmail_password = password_gmail
        from_address = gmail_user

        #para quien va destinado
        to_address = para

        #asunto y mensaje
        asunto = "Test Envio Email"
        mensaje=  'Envio de un correo'
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        	    """ % (from_address, ", ".join(to_address), asunto, mensaje)

        #proceso de login sobre el servidor. Smtp únicamente, imap o pop no
        #porque no queremos recivirlos, unicamente enviar
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_address, to_address, message)
        server.close()

