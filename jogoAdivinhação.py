from random import randint
print()
print('\033[1;36m=================== -> ACERTE O NÚMERO SECRETO!! <- =================== \033[m')
print()
print('\033[;36mSeja bem vindo! Sou seu computador... ')
print()
nome = input('\033[;36mQual é o seu nome?\n\033[;30m--> ')
print()
print('\033[;36mOlá\033[;33m',nome ,'\033[;36mmostre-me do que você é capaz!')
print()
resposta = "S"
while resposta == "S":
    numeroSorteado = randint(1, 10)
    print ()
    tentativas = int(input('\033[;36mCom quantas tentativas você acha que consegue acertar o número secreto?\n\033[;30m--> '))
    print ()
    pontos = int(0)
    print()
    print('\033[;36mAcabei de pensar em um número entre 1 e 10... Você terá' , tentativas , 'tentativas, boa sorte!')
    print()
    while tentativas > 0:
        tentativas = tentativas - 1
        usuario = int(input('\033[;35mQual o seu palpite?\n\033[;30m--> '))
        if usuario > 10:
            print ()
            print ()
            print ("\033[31;40mO número está entre 1 e 10! Por favor digite um número menor...\033[m" , '\033[;33m Número de tentativas: %d\033[;36m' % tentativas)
            print ("\033[31;40mVocê perdeu uma tentativa!\033[m")
            print ()
            print ()
        elif usuario != numeroSorteado:
            print()
            print('\033[;31mOpsss... Você errou, o número secreto era\033[;31m' , numeroSorteado , '!\033[;33m Número de tentativas: %d\033[;36m' % tentativas)
            print ()
            if pontos == 0:
                print('\033[;36mVocê possui 0 pontos!')
                print()
            else:
                pontos = pontos - 1
                print('\033[;36mAgora você possui' , pontos, 'pontos...')
                print()

        else:
            pontos = pontos + 3
            print()
            print('\033[;32mParabéns! Você tem', pontos , 'pontos...' , '\033[;33m Número de tentativas: %d\033[;36m' % tentativas)
            print()
        numeroSorteado = randint(1, 10)
    print()
    print('\033[;36mSuas chances acabaram...' ,'Você fez\033[;32m', pontos ,  'pontos!\033[;36m Obrigado por jogar\033[;33m', nome ,'\033[;36mvolte sempre!')
    print()
    print()
    resposta = input("\033[;36mDigite \"S\" se deseja jogar novamente ou \"N\" se deseja parar:\n--> ").upper()
    print()
    print('=======================================================================')
    