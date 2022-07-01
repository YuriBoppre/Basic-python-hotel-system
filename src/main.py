import json
from time import sleep
import functions
from functools import reduce


def valida_cpf(cpf):
    if len(cpf) != 11:
        return False
    return True


def add_novo_hospede():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)

    value = 1
    while value != 0:
        functions.cls()

        name = input("Informe um nome: ")

        if name == None or name == "":
            print("Nome é obrigatório")
            sleep(1)
            continue

        cpf = input("Informe o cpf: ")

        if cpf == None or cpf == "":
            print("CPF é obrigatório")
            sleep(1)
            continue

        if not valida_cpf(cpf):
            print("CPF inválido")
            sleep(1)
            continue

        qtdePessoas = int(input("Informe quantas pessoas: "))

        if qtdePessoas == None:
            print("Quantidade de pessoas é obrigatório")
            sleep(1)
            continue

        if qtdePessoas <= 0:
            print("Quantidade de pessoas deve ser maior que 0")
            sleep(1)
            continue

        tipoQuarto = input(
            "Informe o quarto desejado(S – Standar, D – Deluxe, P – Premium): "
        )

        if tipoQuarto not in ("S", "D", "P"):
            print("Tipo quarto inválido")
            sleep(1)
            continue

        numDias = int(input("Quantos dias de estadia: "))

        if numDias == None:
            print("quantidade de dias é obrigatório")
            sleep(1)
            continue

        if numDias <= 0:
            print("Quantidade de dias deve ser maior que 0")
            sleep(1)
            continue

        valor = functions.verificaValorDoQuarto(tipoQuarto, qtdePessoas, numDias)

        hospedes_data.append(
            {
                "id": len(hospedes_data) + 1,
                "nome": name,
                "cpf": cpf,
                "qtdePessoas": qtdePessoas,
                "tipoQuarto": tipoQuarto,
                "numDias": numDias,
                "valor": valor,
                "status": "R",
            }
        )

        json.dump(hospedes_data, open("./hospedes.data.json", "w", encoding="utf-8"))
        hospedes_json.close()

        functions.cls()
        print("Hospede adicionado!\n")
        functions.print_dados_hospede(hospedes_data[-1])
        value = int(input("\n1 - Cadastrar novo Hospede\n0 - Sair\n>>"))


def realizar_check_in():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)

    functions.cls()
    print("1 - Buscar Hospede por cpf")
    print("0 - Voltar")

    value = int(input("Escolha uma opção: "))
    while value == 1:
        cpf = int(input("Informe o CPF para a busca: "))

        try:
            reservas_hospede = functions.procurar_reserva_pelo_cpf(hospedes_data, cpf)

            if len(reservas_hospede) == 0:
                print("Valor do cpf inválido")

            reservas_realizadas = tuple(
                filter(lambda x: x["status"] == "R", reservas_hospede)
            )
            id_reserva_para_realizar_check_in = 0

            if len(reservas_realizadas) > 1:
                for reserva_realizada in reservas_realizadas:
                    functions.print_dados_hospede(reserva_realizada)

                id_reserva_para_realizar_check_in = int(
                    input("Digite o id da reserva: ")
                )
            else:
                id_reserva_para_realizar_check_in = int(reservas_realizadas[0]["id"])

            for hospede in hospedes_data:
                if int(hospede["id"]) == id_reserva_para_realizar_check_in:
                    hospede["status"] = "A"
                    print("Check in realizado com sucesso")

            json.dump(
                hospedes_data, open("./hospedes.data.json", "w", encoding="utf-8")
            )
            hospedes_json.close()

        except Exception as e:
            print(e)

        value = int(input("\n 1 - Realizar outra pesquisa\n 0 - Voltar\n>> "))


def realizar_check_out():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)

    functions.cls()
    print("1 - Buscar Hospede por cpf")
    print("0 - Voltar")

    value = int(input("Escolha uma opção: "))
    while value == 1:
        cpf = int(input("Informe o CPF para a busca: "))

        try:
            reservas_hospede = functions.procurar_reserva_pelo_cpf(hospedes_data, cpf)

            reservas_ativas = tuple(
                filter(lambda x: x["status"] == "A", reservas_hospede)
            )
            id_reserva_para_realizar_check_out = 0

            if len(reservas_ativas) > 1:
                for reserva_ativa in reservas_ativas:
                    functions.print_dados_hospede(reserva_ativa)

                id_reserva_para_realizar_check_out = int(
                    input("Digite o id da reserva: ")
                )
            else:
                id_reserva_para_realizar_check_out = int(reservas_ativas[0]["id"])

            for hospede in hospedes_data:
                if int(hospede["id"]) == id_reserva_para_realizar_check_out:
                    hospede["status"] = "F"
                    print("Check out realizado com sucesso")

            json.dump(
                hospedes_data, open("./hospedes.data.json", "w", encoding="utf-8")
            )
            hospedes_json.close()

        except Exception as e:
            print(e)

        value = int(input("\n 1 - Realizar outra pesquisa\n 0 - Voltar\n>> "))


def alterar_reserva():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)

    functions.cls()
    print("1 - Buscar Hospede por cpf")
    print("0 - Voltar")

    value = int(input("Escolha uma opção: "))
    while value == 1:
        cpf = int(input("Informe o CPF para a busca: "))

        try:
            reservas_hospede = functions.procurar_reserva_pelo_cpf(hospedes_data, cpf)

            id_reserva_para_alterar = 0
            if len(reservas_hospede) > 1:
                for reserva_ativa in reservas_hospede:
                    functions.print_dados_hospede(reserva_ativa)

                id_reserva_para_alterar = int(input("Digite o id da reserva: "))
            else:
                id_reserva_para_alterar = int(reservas_hospede[0]["id"])

            print()
            qtdePessoas = int(input("Informe quantas pessoas*: "))
            tipoQuarto = input(
                "Informe o quarto desejado(S – Standard, D – Deluxe, P – Premium)*: "
            )
            numDias = int(input("Quantos dias de estadia: "))
            status = input("status: ")
            valor = functions.verificaValorDoQuarto(tipoQuarto, qtdePessoas, numDias)
            print()

            for hospede in hospedes_data:
                if int(hospede["id"]) == id_reserva_para_alterar:
                    hospede["status"] = status
                    hospede["tipoQuarto"] = tipoQuarto
                    hospede["numDias"] = numDias
                    hospede["valor"] = valor

            json.dump(
                hospedes_data, open("./hospedes.data.json", "w", encoding="utf-8")
            )
            hospedes_json.close()

        except Exception as e:
            print(e)

        value = int(input("\n 1 - Realizar outra pesquisa\n 0 - Voltar\n>> "))


def relatorio_por_cpf():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)

    cpf = int(input("Informe o CPF para a busca: "))
    reservas = functions.procurar_reserva_pelo_cpf(hospedes_data, cpf)

    functions.cls()
    print("Relatório")
    for reserva in reservas:
        functions.print_dados_hospede(reserva)
        print()


def relatorio_por_status(status):
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)
    reservas = functions.listar_reservas_por_status(hospedes_data, status)

    value = 1
    while value == 1:
        functions.cls()
        print("Relatório")
        for reserva in reservas:
            functions.print_dados_hospede(reserva)
            print()
        value = int(input("\n0 - Sair\n>> "))

    functions.cls()


def relatorio_total_recebido():
    hospedes_json = open("./hospedes.data.json")
    hospedes_data = json.load(hospedes_json)
    total = float(reduce(lambda acc, x: acc + x["valor"], hospedes_data, 0))

    functions.cls()
    print("Relatório")
    print(f"O valor total recebido é de {total}")


def mostrar_opcoes_relatorios():
    print("Relatórios")
    print("____________________________________")
    print("1 - Reservas com status R")
    print("2 - Reservas com status C")
    print("3 - Reservas com status A")
    print("4 - Reservas com status F")
    print("5 - Total recebido")
    print("6 - Reservas por CPF")
    print("7 - Sair")


def menu_relatorios():
    mostrar_opcoes_relatorios()
    option = int(input("Escolha um opção: "))

    if option == 1:
        relatorio_por_status("R")
    elif option == 2:
        relatorio_por_status("C")
    elif option == 3:
        relatorio_por_status("A")
    elif option == 4:
        relatorio_por_status("F")
    elif option == 5:
        relatorio_total_recebido()
    elif option == 6:
        relatorio_por_cpf()
    else:
        return

    menu_relatorios()


def show_options():
    print("Palace Hotel")
    print("____________________________________")
    print("1 - Cadastrar uma reserva")
    print("2 - Entrada de cliente (Check in)")
    print("3 - Saída do cliente (check out)")
    print("4 - Alterar reserva")
    print("5 - Relatórios")
    print("6 - Sair")


def main_menu():
    """Função menu recursiva, quando escolhido a opção 6."""
    functions.cls()

    show_options()
    option = int(input("Escolha um opção: "))

    if option == 1:
        add_novo_hospede()
    elif option == 2:
        realizar_check_in()
    elif option == 3:
        realizar_check_out()
    elif option == 4:
        alterar_reserva()
    elif option == 5:
        menu_relatorios()
    else:
        return

    main_menu()


if __name__ == "__main__":
    main_menu()
