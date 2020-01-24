print('*************************')
print('Python Test')
print('*************************')

numero_secreto = 42

chute_str = input("Digite um número: ")

chute = int(chute_str)

print("Você digitou: ", chute)

if (numero_secreto == chute):
    print('Você acertou o número secreto')
else:
    print('você errou o número secreto')