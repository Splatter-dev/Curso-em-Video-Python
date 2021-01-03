## Jogar par ou impar
from random import randint

mnumber = 0
unumber = 0
result = 0
countvictory = 0
option = ""
flag = 0


while True:
    if flag > 0:
        break
    while flag == 0:
        unumber = int(input("\nDigite um numero: "))
        mnumber = randint(1, 10)
        option  = input("\nImpár\nPar\nDigite sua opção[P/I]: ").strip().upper()
        soma = unumber + mnumber
        result = soma % 2 

        if option[0] == "P":
            if result == 0:
                countvictory += 1
                print(f"\nA maquina escolheu {mnumber} e você escolheu {unumber}. O resultado {soma} é PAR! Você ganhou! Vamos para próxima!\n")
            else:    
                print(f"A maquina escolheu {mnumber} e você escolheu {unumber}. O resultado {soma} é IMPAR! Você perdeu! Jogo encerrado !\n")
                flag += 1 

        if option[0] == "I":
            if result > 0:
                countvictory += 1
                print(f"\nA maquina escolheu {mnumber} e você escolheu {unumber}. O resultado {soma} é IMPAR! Você ganhou! Vamos para próxima!\n")
            else:
                print(f"A maquina escolheu {mnumber} e você escolheu {unumber}. O resultado {soma} é PAR! Você perdeu! Jogo encerrado !\n")
                flag += 1

print(f"\nVocê ganhou {countvictory} vezes")

