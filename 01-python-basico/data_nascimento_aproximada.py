from datetime import date, timedelta
idade = int(input("Digite sua idade: "))
mes = int(input("Digite o número do mês do seu nascimento (1 a 12): "))
dia = int(input("Digite o dia do seu nascimento: "))
hoje = date.today()
ano = hoje.year - idade
try:
    nascimento = date(ano, mes, dia)
    if nascimento > hoje:
        nascimento = date(ano - 1, mes, dia)
    print(f"Sua data de nascimento aproximada é: {nascimento.strftime('%d/%m/%Y')}")
except ValueError:
    print("Data inválida. Verifique os valores digitados.")
