import random

def jogar():

    print("Bem vindo a Forca!")
    print("------------------") 

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_certas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6
    rodadas = 0

    print(letras_certas) 

    while(not enforcou and not acertou):


        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas [index] = letra
                index = index + 1
                
        else:
                erros = erros + 1

        rodadas = rodadas + 1  
        tentativas = tentativas - 1
        enforcou = erros == 6
        acertou = "_" not in letras_certas 
        print(letras_certas)  
        if (acertou):
            print(" Você venceu com {} tentativas!!".format(rodadas))  
        elif(enforcou):
            print("Que pena!")
        else:
            print(" Você tem mais {} tentativas".format(tentativas)) 


    if(acertou):
        print("Parabens!")
    else:
        print("Você perdeu!")


if(__name__ == "__main__"):
    jogar()

