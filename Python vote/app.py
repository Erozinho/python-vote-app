from rich import print
import os
#Constantes
VOTOS_SP = 0
VOTOS_RJ = 0
#codigo sempre ativo
while True:
    try:
        #apresentar as opçoes
        print("**********\n[on blue]TOTAL SP:[/] {}\n[on red]TOTAL RJ:[/] {}\n***********".format(VOTOS_SP,VOTOS_RJ))
        #permitir o voto
        voto = int(input("Qual seria seu voto?\n1-SP\n2-RJ\nSeu voto: "))
        if voto == 1: VOTOS_SP += 1
        elif voto == 2 : VOTOS_RJ += 1
        elif voto == 120: break
        else: pass
    except:
        print("Digite apenas 1 ou 2!")
    os.system("cls")