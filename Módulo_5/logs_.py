import logging
""" 
debug
info
warning
error
critical
"""


def email_correto():
    if email == 'x@gmail.com':
        return True
    else:
        return False

def senha_correta():
    if senha == 1234:
        print('Login feito com sucesso')
        logging.info(f'{email} entrou em sua conta bancária')
        return True
    else:
        print('Senha incorreta, tente novamente')
        return False

logging.basicConfig(level=logging.DEBUG, 
filename='app.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = str(input('Digite seu email: \n'))
    senha = int(input('Digite sua senha: \n'))
    email_correto()
    senha_correta()
        
except False:
    print('Por favor, verifique se o e-mail está correto.')
except ValueError as erro:
    print('Digite apenas números')
    logging.error(erro)