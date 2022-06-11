import json
from math import ceil
from posixpath import split
import src.functions as functions

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
        
        
class Option:
    def __init__(self, value: str):
        start = 1
        end = 6
        valid_options = [str(x) for x in range(start, end + 1)]
        if value not in valid_options:
            raise ValueError("O valor digitado deve ser uma opção válida")
        self.value = int(value)
        
def get_option_from_user():
    try:
        value = input("Escolha uma opção: ")
        return Option(value)
    except ValueError:
        print("Opção inválida")
        get_option_from_user()

def show_options():
    print('Palace Hotel')
    print('____________________________________')
    print('1 - Cadastrar uma reserva')
    print('2 - Entrada de cliente (Check in)')
    print('3 - Saída do cliente (check out)')
    print('4 - Alterar reserva')
    print('5 - Relatórios')
    print('6 - Sair')

def main_menu():
    """Função menu recursiva, quando escolhido a opção 6."""
    functions.cls()

    show_options()
    option = get_option_from_user()

    if option.value == 1:
        add_novo_hospede()
    elif option.value == 2:
        realizar_check_in()
    elif option.value == 3:
        ...
    elif option.value == 4:
        ...
    elif option.value == 5:
        ...
    else:
        return

    main_menu()

if __name__ == "__main__":
    main_menu()