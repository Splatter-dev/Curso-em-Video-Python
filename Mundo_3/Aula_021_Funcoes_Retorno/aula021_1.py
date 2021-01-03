# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(s)


# somar(a=1, b=25)


# na função, se eu colocar a=0 o valor do parametro  passado para dentro da função se torna opcional.


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(s)
#     return s


# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)

# print(f"Os valores foram {r1}, {r2} e {r3}")


# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f        


# r1 = fatorial(5)
# r2 = fatorial(4)
# r3 = fatorial()
# print(r1,r2,r3)


def par(n=0, n2=0):
    if n % 2 == 0:
        return True
    else:
        return False


num =  int(input("Digite um numero: "))
if par(num):
    print("É par!")
else:
    print("É impar!")            