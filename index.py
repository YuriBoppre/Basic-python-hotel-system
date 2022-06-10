import json
from math import ceil
from posixpath import split
import functions

hospedes_json = open('./hospedes.data.json')

hospedes_data = json.load(hospedes_json)

    
def add_novo_hospede():
    value = 1
    while value != 0:
        functions.cls()
        name = input('Informe um nome*: ')
        cpf = int(input('Informe o cpf*: '))
        qtdePessoas = int(input('Informe quantas pessoas*: '))
        tipoQuarto = input('Informe o quarto desejado(S – Standar, D – Deluxe, P – Premium)*: ')
        numDias = int(input('Quantos dias de estadia: '))
        valor = functions.verificaValorDoQuarto(tipoQuarto, qtdePessoas, numDias)
        status = input('status: ')

        hospedes_data.append({
            'id': len(hospedes_data) + 1,
            'nome': name,
            'cpf': cpf, 
            'qtdePessoas': qtdePessoas,
            'tipoQuarto': tipoQuarto,
            'numDias': numDias,
            'valor': valor,
            'status': status
            })
        
        json.dump(hospedes_data, open('./hospedes.data.json', 'w', encoding='utf-8'))
        functions.cls()
        print('Hospede adicionado!\n')
        functions.print_dados_hospede(hospedes_data[-1])
        value = int(input('\n1 - Cadastrar novo Hospede\n0 - Sair\n>>'))

def realizar_check_in():
    """
    Buscando CPF para realizar check in.
    """
    value = 1
    while value != 0:
        functions.cls()
        print('1 - Buscar Hospede por cpf')
        print('0 - Voltar')
        value = int(input('Escolha uma opção: '))
        if value == 1:
            cpf = int(input('Informe o CPF para a busca: '))
            try: functions.print_dados_hospede(functions.procurar_reserva_pelo_cpf(hospedes_data, cpf))
            except Exception as e:print(e)
        value = int(input('\n 1 - Realizar outra pesquisa\n 0 - Voltar\n>> '))


def main_menu():
    """
    Função menu recursiva, fecha apenas quando digitado zero 0.
    """
    value = 1
    functions.cls()
    print('Palace Hotel')
    print('________')
    print('1 - Cadastrar uma reserva')
    print('2 - Entrada de cliente (Check in)')
    print('3 - Saída do cliente (check out)')
    print('4 - Alterar reserva')
    print('5 - Relatórios')
    print('6 - Sair')
    try: value = int(input('Escolha uma opção: '))
    except: main_menu()
    if value == 1:
        add_novo_hospede()
    if value == 2:
        realizar_check_in()
    if value == 3:
        a()
    if value == 4:
        a()
    if value == 5:
        a()
    if value == 6:
        return
    else: main_menu()

main_menu()