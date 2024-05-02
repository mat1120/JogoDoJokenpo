import random
from time import sleep
print("\033[0;33m-=-\033[m"*20)
print("VAMO JOGAR JOKENPO")
print("\033[0;33m-=-\033[m"*20)
opcoes = ["pedra".lower(),"tesoura".lower(),"papel".lower()]
computador = random.choice(opcoes)
jogador = input("QUAL VOCE VAI JOGAR? ESCOLHA PEDRA,PAPEL OU TESOURA:").strip().lower()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
if jogador == computador:
    print("\033[0;34mEMPATAMOS\033[m")
elif jogador == "pedra":
    if computador == "tesoura":
        print("\033[0;32mVOCE GANHOU!PEDRA ESMAGA TESOURA\033[m")
    else:
        print("\U0001F60E\033[0;31mVOCE PERDEU!PAPEL COBRE PEDRA\033[m")
elif jogador == "papel":
    if computador == "pedra":
        print("\033[0;32mVOCE GANHOU!PAPEL COBRE PEDRA\033[m")
    else:
        print("\U0001F60E\033[0;31mVOCE PERDEU!TESOURA CORTA PAPEL\033[m")
elif jogador == "tesoura":
    if computador == "papel":
        print("\033[0;32mVOCE GANHOU!TESOURA CORTA PAPEL\033[m")
    else:
        print("\U0001F60E\033[0;31mVOCE PERDEU!PEDRA ESMAGA TESOURA\033[m")




