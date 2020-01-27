import random

print('*************************')
print('Python Test - Número Secreto')
print('*************************')

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0
rodada = 1

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina um nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)
    print("Você digitou: ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print('Show! Você acertou o número secreto!')
        break
    else:
        if(chute_maior):
            print('Você errou! O seu número é maior que o número secreto.')
        elif(chute_menor):
            print('Você errou! O seu número é menor que o número secreto.')

print("Fim do jogo!")