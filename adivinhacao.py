print('*************************')
print('Python Test - Número Secreto')
print('*************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número: ")
    chute = int(chute_str)
    print("Você digitou: ", chute)

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print('Show! Você acertou o número secreto!')
    else:
        if(chute_maior):
            print('Você errou! O seu número é maior que o número secreto.')
        elif(chute_menor):
            print('Você errou! O seu número é menor que o número secreto.')

print("Fim do jogo!")