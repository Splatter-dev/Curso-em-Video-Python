def valid(p):
    """[summary]

    Args:
        p ([type]): [description]

    Returns:
        [type]: [description]
    """
    while True:
        valor = str(input(p)).strip()
        newv = valor
        if "," in newv:
            newv = newv.replace(",","")
        elif "." in newv:
            newv = newv.replace(".","")    
        if newv == "" or not newv.isnumeric():
            print(f'\033[31mERRO! "{newv}" é um preço inválido!\033[m')      
        else:
            break       
    if "," in valor:
        valor = valor.replace(",",".")    
    return float(valor)