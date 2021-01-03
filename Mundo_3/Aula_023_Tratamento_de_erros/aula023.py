try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r =  a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados digitados.")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0")
except KeyboardInterrupt:
    print("O usúario encerrou o programa!")
except Exception as error:
    print(f"O erro encontrado foi: {error.__cause__}")                
else:
    print(f"O resultado é: {r:.1f}")    
finally:
    print("Volte sempre :)")    