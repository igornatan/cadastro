from Pessoa import Pessoa
from Contato import Contato
from Residencia import Residencia
from Identificacao import Identificacao
from Profissional import Profissional


def main():
    casa = Residencia('88888-000', 'Avenida', 'Getúlio Vargas', '80', 'Centro', None, 'Chapecó')
    contato = Contato('(49) 99999-9999', 'Particular', 'teste@teste.com', 'Comercial')
    identificacao = Identificacao('Igor Bagio', '111.222.333-44', 'Masculino', 'Solteiro', '19/08/1999', 'Xaxim/SC')
    profissional = Profissional('Desenvolvedor', 'Graduando', '1.000,00')
    Igor = Pessoa(identificacao, profissional, casa, contato)

    print(Igor.get_contato.get_email)


if __name__ == '__main__':
    main()