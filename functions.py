from math import ceil
import os
from logging import exception


def cls():
    """
    Limpa a tela.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_dados_hospede(hospede):
    """
    Print dados do hospede.
    """
    print(f"""id: {hospede['id']}\tnome: {hospede['nome']}\tcpf: {hospede['cpf']}\tTipo do quarto: {hospede['qtdePessoas']}\tTipo quarto: {hospede['tipoQuarto']}
    \tQtde. dias: {hospede['numDias']}\tValor: {hospede['valor']}\tStatus: {hospede['status']}""")
   
   
    # print('id: %s\tnome: %s\tcpf: %s\tQtde. pessoas: %s\tTipo do quarto: %s\tDias: %s\tValor: %s\tStatus: %s' %
    #       (hospede['id'], hospede['nome'], hospede['cpf'], hospede['qtdePessoas'], hospede['tipoQuarto'], hospede['numDias'], hospede['valor'], hospede['status']))


def verificaValorDoQuarto(tipoQuarto, qtdePessoas, dias):
    """
    Calculando valores
    """
    if(tipoQuarto.upper() == 'S'):
        return dias * (qtdePessoas * 100) 
    if(tipoQuarto.upper() == 'D'):
        return dias * (qtdePessoas * 200) 
    if(tipoQuarto.upper() == 'P'):
        return dias * (qtdePessoas * 300)


def procurar_reserva_pelo_cpf(lista_hospedes, cpf):
    reservas_pelo_hospede = []

    for hospede in lista_hospedes:
        if hospede['cpf'] == cpf:
            if hospede['status'] == "R":
                reservas_pelo_hospede.append(hospede)

    return reservas_pelo_hospede



    #   reserva_pelo_hospede = []
    #     for hospede in lista_hospedes:
    #     if hospede['status'] == "R" and hospede['cpf'] == cpf:
    #        reserva_pelo_hospede.append(hospede)
    #        return reserva_pelo_hospede