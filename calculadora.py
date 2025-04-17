import math
import os


def adicao():
    result: float = 0
    str_value: str = ''
    while True:
        valor = input("Digite um número (ou pressione Enter para sair): ")
        if valor == '':
            os.system("cls")
            print(f"{str_value}")
            print(f"Valor final: {result}")
            return result
        try:
            numero = float(valor)
            str_value += f" + {numero}"
            result += numero
            print(f"Resultado: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")


def subtracao():
    result: float = 0
    str_value: str = ''
    while True:
        valor = input("Digite um número (ou pressione Enter para sair): ")
        if valor == '':
            os.system("cls")
            print(f"{str_value}")
            print(f"Valor final: {result}")
            return result
        try:
            numero = float(valor)
            str_value += f" - {numero}"
            result -= numero
            print(f"Resultado: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")
       
def multiplicacao():
    result: float = 1
    str_value: str = ''
    while True:
        valor = input("Digite um número (ou pressione Enter para sair): ")
        if valor == '':
            os.system("cls")
            print(f"{str_value}")
            print(f"Valor final: {result}")
            return result
        try:
            numero = float(valor)
            str_value += f" x {numero}"
            result *= numero
            print(f"Resultado: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")


def divisao():
    result: float = 1
    str_value: str = ''
    while True:
        valor = input("Digite um número (ou pressione Enter para sair): ")
        if valor == '':
            os.system("cls")
            print(f"{str_value}")
            print(f"Valor final: {result}")
            return result
        try:
            numero = float(valor)
            str_value += f" / {numero}"
            result = result / numero
            print(f"Resultado: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")


def restoDivisao():
    result: float = 1
    str_value: str = ''
    while True:
        valor = input("Digite um número (ou pressione Enter para sair): ")
        if valor == '':
            os.system("cls")
            print(f"{str_value}")
            print(f"Valor final: {result}")
            return result
        try:
            numero = float(valor)
            str_value += f" % {numero}"
            result = result % numero
            print(f"Resultado: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")


def potenciacao():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} ^ {expoente} = {resultado}")
    return resultado


def raiz_quadrada():
    numero = float(input("Digite o número: "))
    if numero < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo.")
        return None
    resultado = math.sqrt(numero)
    print(f"√{numero} = {resultado}")
    return resultado


def radiciacao():
    radicando = float(input("Digite o radicando: "))
    indice = float(input("Digite o índice da raiz: "))
    if radicando < 0 and indice % 2 == 0:
        print("Não é possível calcular a raiz de índice par de um número negativo.")
        return None
    resultado = math.pow(radicando, 1/indice)
    print(f"{indice}√{radicando} = {resultado}")
    return resultado


def conversao():
    option = int(input("0 - Voltar\n1 - Celcius\n2 - Kelvin\n3 - Fahrenheit \nEscolha: "))
    if option == 0:
        print("<- Voltar")
    elif option == 1:
        temperatura: float = float(input("Graus Celcius: "))
        opt: int = int(input("Temperatura pra converter:\n0 - Cancelar\n1 - Kelvin\n2 - Fahrenheit \nEscolha: "))
        if opt == 0:
            print("<- Voltar")
        elif opt == 1:
            print(f"Celcius para Kelvin = {temperatura + 273}°")
        elif opt == 2:
            print(f"Celcius para Fahrenheit = {temperatura * (9/5) + 32}°")
    elif option == 2:
        temperatura: float = float(input("Graus Kelvin: "))
        opt: int = int(input("Temperatura pra converter:\n0 - Cancelar\n1 - Celcius\n2 - Fahrenheit \nEscolha: "))
        if opt == 0:
            print("<- Voltar")
        elif opt == 1:
            print(f"Kelvin para Celcius = {temperatura - 273}")
        elif opt == 2:
            print(f"Kelvin para Fahrenheit = {(temperatura - 273) * (9/5) + 32}")
    elif option == 3:
        temperatura: float = float(input("Graus Fahrenheit: "))
        opt: int = int(input("Temperatura pra converter:\n0 - Cancelar\n1 - Celcius\n2 - Kelvin \nEscolha: "))
        if opt == 0:
            print("<- Voltar")
        elif opt == 1:
            print(f"Fahrenheit para Celcius = {(temperatura - 32) / (9/5)}")
        elif opt == 2:
            print(f"Fahrenheit para Kelvin = {(temperatura - 32) * (5/9) + 273.15}")
       


menu: int = 100
while menu != 0:
    print("Calculadora Científica Python")
    print("Opções disponíveis:\n0 - Fechar \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Resto de Divisão \n6 - Potenciação \n7 - Raiz Quadrada \n8 - Radiciação \n9 - Conversão")
    menu = int(input("Opção: "))
    if menu == 1:
        adicao()
    elif menu == 2:
        subtracao()
    elif menu == 3:
        multiplicacao()
    elif menu == 4:
        divisao()
    elif menu == 5:
        restoDivisao()
    elif menu == 6:
        potenciacao()
    elif menu == 7:
        raiz_quadrada()
    elif menu == 8:
        radiciacao()
    elif menu == 9:
        conversao()
