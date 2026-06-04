# Exercício simples de senha usando while, if/elif e validação básica.

while True:
    tipo = int(input("Qual o tipo da senha? 1 para números, 2 para letras: "))

    if tipo == 1:
        senha = int(input("Grave uma senha apenas com números: "))

        while True:
            try:
                tentativa = int(input("Qual a senha?: "))
                if tentativa == senha:
                    print("Senha correta! Prossiga...")
                    break
                print("Senha incorreta. Tente novamente...")
            except ValueError:
                print("São permitidos apenas números!")
        break

    elif tipo == 2:
        senha = input("Grave uma senha apenas com letras: ")

        while True:
            tentativa = input("Qual a senha?: ")
            if tentativa == senha:
                print("Senha correta! Prossiga...")
                break
            print("Senha incorreta. Tente novamente...")
        break

    else:
        print("Opção inválida. Escolha 1 para números ou 2 para letras.")
