#Não lembro como funciona, mas parece funcionar
#Vetor

vetor1 = [1, 2, 3, 4]
print(vetor1)
print(vetor1[3])

vetor2 = [0]*5
print(vetor2[4])

vetor2[0] = 2
print(vetor2)
vetor2[1] = 6
print (vetor2)

matriz1 = [ [5,4,10], [4,5,6], [70,10,9]]
print(matriz1)

vetora = [1,4,7]
vetorb = [4,5,2]

matriz2 = [vetora, vetorb]
print(matriz2)

vetorc = ["Bom dia", "Boa noite"]
print(vetorc)

def nota():
  notas = [0]*5
  quant_alunos = 5
  i = 0
  while i >=quant_alunos:
    notas[i] = int(input())
    print (notas)
    i = i +1