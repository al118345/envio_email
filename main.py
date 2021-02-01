# This is a sample Python script.
from envio_email.envio_email import SendEMail


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hola, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('1938web')
    print('El siguiente programa sirve para realizar un envio por gmail.')
    print('En este ejemplo, enviamos un email al correo 1938web@gmail.com')
    enviar_email = SendEMail()
    enviar_email.send_email_test('1938web@gmail.com')
    print('El proceso a finalizado. Un saludo.')



