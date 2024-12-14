# Faca um programa que peca dois numeros ao usuario e mostre qual o maior e qual o menor

primeiro = int(input("Digite o primeiro numero: ")) # centro de armazenagem do primeiro comando
print(primeiro)

segundo = int(input("Digite o segundo numero: ")) # centro de armazenagem do segundo comando
print(segundo)

if segundo > primeiro:
    print("segundo maior")

    #CONCATENACAO
    print("primeiro e maior" + str(primeiro))

    #F STRING
    print(f"primeiro e maior {primeiro}")

else:
    print("primeiro maior")

# Escreva um programa em Python que recebe um inteiro e diga se e par ou impar

numero = int(input("Digite o numero: "))
print(primeiro)

if numero % 2 == 0:
    print("O numero e par")
else:
    print("O numero e par")

# Codigo que pergunte o estado civil de uma pessoa 
# "C" (CASADO) "S" SOLTEIRO "D" DIVORCIADO "V" VIUVO "O" OUTROS

estado_civil = input ("informe o estado civil")
if estado_civil == "D":
    print("Divorciado")
elif estado_civil == "S":
    print("Solteiro")
elif estado_civil == "V":
    print("Viuvo")
elif estado_civil == "C":
    print("Casado")
else:
    print("Outros")