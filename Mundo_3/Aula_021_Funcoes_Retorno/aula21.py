def contador(i, f, p):
    """sumary_line
    i = inicio
    f = fim
    p = passo
    """
    c = i
    while c < f:
        c += p
        print(c)




contador(1, 10, 1)

help(contador)