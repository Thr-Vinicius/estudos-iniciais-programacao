import time
alunos = 0
for alunos in range(2):
    n_aluno = input("Informe o nome do aluno: ")
    nt1_aluno = int(input(f"Informe a nota do primeiro trimestre do aluno {n_aluno}: "))
    nt2_aluno = int(input(f"Informe a nota do segundo trimestre do aluno {n_aluno}: "))
    nt3_aluno = int(input(f"Informe a nota do terceiro trimestre do aluno {n_aluno}: "))
    while not (0 <= nt1_aluno <= 100 and 0 <= nt2_aluno <= 100 and 0 <= nt3_aluno <= 100):
        print("Valor inválido, as notas devem estar entre 0 e 100.")
        nt1_aluno = int(input(f"Informe a nota do primeiro trimestre do aluno {n_aluno}: "))
        nt2_aluno = int(input(f"Informe a nota do segundo trimestre do aluno {n_aluno}: "))
        nt3_aluno = int(input(f"Informe a nota do terceiro trimestre do aluno {n_aluno}: "))
    else:
        nt_total = (nt1_aluno + nt2_aluno + nt3_aluno) / 3
        if nt_total >= 60:
            print("Aluno aprovado! Média = ",nt_total)
        else:
            print("Aluno reprovado... Média = ",nt_total)