#Simples. Funcionou
#Nota

from pickle import TRUE


nota = int(input("NOTA"))
comportamento = bool(input("Comportamento"))

if (nota >=60 and comportamento == 1):
    print("aprovado")
else:
    print("reprovado")

