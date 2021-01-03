# Mostrar vogais das palavras

words = ("Cafe","Teste","Piscina","Doida")
# lastWord = len(words)
inspectWord = ""


for words in words:
    inspectWord = words.upper()
    print(f"\nNa palavra {inspectWord} temos as vogais: ",end='')
    if "A" in inspectWord:
        # print(inspectWord.count("A"))
        print("a",end=' ')
    if "E" in inspectWord:
        print("e",end=' ')     ### Meu Programa
    if "I" in inspectWord:
        print("i",end=' ')      
    if "O" in inspectWord:
        print("o",end=' ')
    if "U" in inspectWord:
        print("u")
print("\n")        

for word in words:
    print(f"\nNa palavra {word} temos as vogais: ",end='')
    for l in word:
        if l.lower() in "aeiou":                            ## Programa do professor
            print(f"{l}",end=" ")
print("\n")            
    