# Digitar um numero e fatorar.

num = int(input("\nDigite um numero: "))

result = num
print("{}! = ".format(result), end='')

while num != 0:
    print(" {} ".format(num), end="") 
    print("x " if num > 1 else " = ", end="" ) 
    num -= 1
    if num != 0:
        result = result * num  
print(result, "\nO resultado da fatoração é {}.".format(result))
