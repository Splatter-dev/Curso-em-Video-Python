def moeda(valor=0, moeda="R$"):
    valorFormat = (f"{moeda}{valor:.2f}")
    if "." in valorFormat:
        valorFormat = valorFormat.replace(".",",")
    return valorFormat
