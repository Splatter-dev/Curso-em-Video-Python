tupla = (
"Zero",
"Um",
"Dois",
"Três",
"Quatro",
"Cinco",
"Seis",
"Sete",
"Oito",
"Nove",
"Dez",
"Onze",
"Doze",
"Treze",
"Quatorze",
"Quinze",
"Dezeseis",
"Dezesete",
"Dezoito",
"Dezenove",
"Vinte"
)


while True:
    num = int(input("Digite um numero de 0 à 20 [Aperte Ctrl + D para sair]: "))
    if num < 0 or num > 20:
        print("Valor incorreto.")
    else:    
        print(f"{tupla[num]}")
        # break