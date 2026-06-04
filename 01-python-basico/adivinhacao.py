# Como Adivinhar ? (Python)

numero = 9 
chute = int(input("Adivinhe o valor:"))
            
while bool(chute) is True:
  if (numero == chute):
   print ("correto")
   break
  print("você errou, tente novamente:")
  chute = int(input())

print ("BLUE SCREAM #000456")
