import random

def jogar():

    print("Bem vindo ao Adivinhados!")
    print("-------------------------")

    print("Dificuldades:")
    print("facil = 1")
    print("medio = 2")
    print("dificil = 3")
    print("-------------------------")

    dificuldade = input("Digite a dificuldade: ")
    numero_rodadas = int(dificuldade)

    if(numero_rodadas == 1):
        tentativas = 15
    elif(numero_rodadas == 2):
        tentativas = 10
    elif(numero_rodadas == 3):
        tentativas = 5
    else:
        print("dificuldade invalida")



    numero_secreto = random.randrange(1,101)
    rodadas = 0
    num_max = 100
    num_min = 1
    pontos = 1000
    x = 0

    for rodadas in range(0, tentativas):

        tentativas = tentativas - 1
        chute = input("Digite seu numero: ")
        numero = int(chute)

        if(numero > num_max or numero < num_min):
            print("Você tem:",tentativas,"tentativas")
            print("Número Inválido -1 tentátiva")
            continue
        else:

            acertou = numero_secreto == numero 
            maior = numero_secreto > numero
            rodadas = rodadas + 1

            if (acertou):
                    tentativas = 0
                    print ("Você acertou em: {} rodada(s)".format(rodadas))
                    break
            else:
                print("Você tem:",tentativas,"tentativas")
                if (maior):
                        print ("Você Errou! O numero e maior")
                        x = numero_secreto - numero
                        pontos = pontos - x
                else:
                        print ("Você Errou! O numero e menor")
                        x = numero_secreto - numero
                        pontos = pontos - x

    print("Sua pontuação foi de",pontos)
    print ("O numero era",numero_secreto,"Fim de jogo") 