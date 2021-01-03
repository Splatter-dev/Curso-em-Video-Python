from time import sleep


def adiciona(frase):
    tam = len(frase) + 4
    print("~" * tam)
    sleep(1)
    print(f"  {frase}")
    sleep(1)
    print("~" * tam)

adiciona("OLÁ")
adiciona("PAULO VITOR")
adiciona("SEJA BEM-VINDO(A)")
