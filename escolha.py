import adivinhação
import forca


print("Escolha o jogo para se divertir!")
print("--------------------------------")

print("Aivinhados = 1")
print("Forca = 2")
print("--------------------------------")



jogo = int(input("qual o código do jogo?"))

if(jogo == 1):
    print("-------------------------")
    adivinhação.jogar()
elif(jogo == 2):
    print("------------------")
    forca.jogar()
else:
    print("Código inválido")