# Algoritmo desenvolvido para auxiliar atendentes da companhia aérea Sweet Flight no controle de aeronaves, assentos e reservas de passagens.
import os
os.system("cls || clear")
from dataclasses import dataclass
import time

# Dois vetores para armazenar os dados
lista_aviao = []
lista_assento = []

# Um vetor para as reservas.
lista_reserva = []

# Total de aviões.
QTD_AVIAO = 4

# Total de reservas permitidas.
TOTAL_RESERVAS = 20

@dataclass
class Reserva:
    numero_aviao: str
    nome_passageiro: str

# FUNÇÃO PARA REGISTAR AS QUANTIDADES
def registrar_avioes(lista_aviao):
    print("------ REGISTRO DE AVIÃO ------")
    for aviao in (QTD_AVIAO):
        numero_aviao = input(f" INFORME O NÚMERO DO {aviao}° AVIÃO: ")
        lista_aviao.append(numero_aviao)
    print("Aviões registrados com sucesso!")
    
def registrar_assento(lista_assento):
    if not lista_aviao:
        print("\nRegistre os aviões (opção 1)!\n")
        return
    lista_assento.clear()

    print("------ REGISTRO DE ASSENTOS ------")
    for assento in (QTD_AVIAO):
        quantidade_assento = input(f" INFORME A QUANTIDADE DE ASSENTOS DISPONÍVEIS NO {assento}° AVIÃO: ")
        
        lista_assento.append(quantidade_assento)
        
        print("Quantidade de assentos registrados com sucesso!\n")

def reservar_passagem():
    print("\n--- RESERVA DE PASSAGEM ---")

    if not lista_aviao or not lista_assento:
        print("Antes registre aviões e assentos! (opções 1 e 2)\n")
        return

    if len(lista_reserva) >= TOTAL_RESERVAS:
        print("Limite máximo de 20 reservas atingido!\n")
        return

    numero = input("Digite o número do avião: ")

    if numero not in lista_aviao:
        print("Este avião não existe!\n")
        return

    indice = lista_aviao.index(numero)

    if lista_assento[indice] == 0:
        print("Não há assentos disponíveis para este avião!\n")
        return

    nome = input("Digite o nome do passageiro: ")

    reserva = Reserva(numero_aviao=numero, nome_passageiro=nome)
    lista_reserva.append(reserva)

    lista_assento[indice] -= 1

    print("Reserva realizada com sucesso!\n")

def encontrar_por_aviao():
    print("\n--- CONSULTA POR AVIÃO ---")
    numero = input("Informe o número do avião: ")

    if numero not in lista_aviao:
        print("Este avião não existe!\n")
        return

    achou = False
    print(f"\nReservas para o avião {numero}:")
    for reserva in lista_reserva:
        if reserva.numero_aviao == numero:
            print(f"- {reserva.nome_passageiro}")
            achou = True

    if not achou:
        print("Não há reservas realizadas para este avião!\n")
    else:
        print()

def encontrar_por_nome():
    print("\n--- CONSULTA POR PASSAGEIRO ---")
    nome = input("Informe o nome do passageiro: ")

    achou = False
    print(f"\nReservas encontradas para {nome}:")
    for reserva in lista_reserva:
        if reserva.nome_passageiro.lower() == nome.lower():
            print(f"- Avião: {reserva.numero_aviao}")
            achou = True

    if not achou:
        print("Não há reservas realizadas para este passageiro!\n")
    else:
        print()

while True:

    print("============== Sweet Flight ==============")
    print("(1) Registrar Número do Avião")
    print("(2) Registrar Assentos Disponíveis Avião")
    print("(3) Reservar Passagem Aérea")
    print("(4) Realizar Consulta Por Avião")
    print("(5) Realizar Consulta Por Passageiro")
    print("(6) Encerrar ")
    print("\n")

    try: 
        opcao = input("R: ")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    if opcao == "1":
        registrar_avioes()
    elif opcao == "2":
        registrar_assento()
    elif opcao == "3":
        reservar_passagem()
    elif opcao == "4":
        encontrar_por_aviao()
    elif opcao == "5":
        encontrar_por_aviao()
    elif opcao == "6":
        print("Encerrando sistema.")
        break
    else:
        print("Opção inválida! Tente novamente.\n")

    if opcao != 1 and opcao != 0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")