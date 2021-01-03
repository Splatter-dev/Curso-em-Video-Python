def fatorial(num=1, show=False):
    """[summary]
    Args:
        num (int, optional): [Número a ser calculado passado pela variavel num]. Defaults to 1.
        show (bool, optional): [Mostrar ou não a conta]. Defaults to False.
    Returns:
        [type]: [O valor fatorial do número da várial num]
    """
    f = 1
    print("-" * 30)
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f"{c} ", end="")
            if c > 1:
                print("x", end=" ")
            print("=", end=" ")
    return f


num = int(input("Digite um número: "))
result = fatorial(num, False)
print(result)
