# Tabuada

num = int(input("\nTABUATADA!!\nDigite um numero: "))
resul = 0
 
print("-=-" * 4)
for m in range(1, 10 + 1):
    resul = num * m
    print("{} x {} = {}".format(num, m, resul))
print("-=-" * 4)
