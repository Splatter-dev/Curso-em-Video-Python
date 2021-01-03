def moeda(valor):
    valorFormat = (f"R${valor:.2f}").replace(".", ",")
    return valorFormat
   