# Criando uma Calculadora
from decimal import Decimal

print("Escolha de 1 a 4, qual operação deseja fazer")
resposta = str(input("Soma --> 1 \nMenos --> 2 \nMultiplicação --> 3\nDivisão --> 4\n:"))
print("================================================")

numero1 = Decimal(input("Digite o primeiro numero: "))
print("================================================")
numero2 = Decimal(input("Digite o segundo numero: "))
print("================================================")

def calc(n1,n2):
    if resposta == "1":
        return (n1 + n2)
    elif resposta == "2":
        return (n1 - n2)
    elif resposta == "3":
        return (n1 * n2)
    elif resposta == "4":
        if numero1 == 0:
            print("Divisão não permitida por zero")
        elif numero1 != 0:
            return (n1 / n2)
    else:
        return "Declaraçoes numericas invalidas"
    
print(f'Resultado: {calc(numero1, numero1)}')
print("================================================")