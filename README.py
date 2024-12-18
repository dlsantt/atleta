from datetime import datetime

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Entre com o valor para {nome_variavel} do atleta: ')
    while valor_lido == '':
        print(f'O valor para {nome_variavel} não pode ser vazio!')
        valor_lido = input(f'Entre com o valor para {nome_variavel} do atleta: ')
    return valor_lido

def verifica_data_valida(data_texto):
    try:
        data_valida = datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except:
        return False

def ler_data_valida():
    dataNascimentoString = input('Entre com a data de nascimento: ')
    while not verifica_data_valida(dataNascimentoString):
        print('Data inválida!')
        dataNascimentoString = input('Entre com a data de nascimento: ')
    dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")

    return dataNascimento

def ler_atleta():
    nome = ler_valor_nao_vazio('nome')
    especie = ler_valor_nao_vazio('espécie')
    dataNascimento = ler_data_valida()
    tutor = ler_valor_nao_vazio('nome do tutor')

    atleta = {
        'nome': nome,
        'especie': especie,
        'dataNascimento': dataNascimento,
        'tutor': tutor
    }

    return atleta

def imprimir_atleta(atleta):
    print(f"Nome:\t\t{atleta['nome']}")
    print(f"Espécie:\t{atleta['especie']}")
    print(f"Data:\t\t{atleta['dataNascimento'].strftime('%d/%m/%Y')}")
    print(f"Tutor:\t\t{atleta['tutor']}")

meu_atleta = ler_atleta()
meu_outro_atleta = ler_atleta()
imprimir_atleta(meu_atleta)
imprimir_atleta(meu_outro_atleta)
