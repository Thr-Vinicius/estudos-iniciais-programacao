import pyautogui
import time

# ⏲️ Delay para você posicionar a tela antes do programa começar
print("Você tem 5 segundos para posicionar a tela...")
time.sleep(5)

# 🎯 Coordenadas configuráveis
coord_codigo = (500, 300)       # Exemplo: coordenada do campo de código
coord_quantidade = (600, 300)   # Exemplo: coordenada do campo de quantidade
coord_cpo = (700, 300)          # Exemplo: coordenada do campo de CPO

# 🔁 Mapeamento de CPOs (configure conforme necessário)
mapa_cpo = {
    "5950": "1405"
    # Adicione mais se quiser
}

# 1️⃣ Quantos produtos serão cadastrados
qtd = int(input("Quantos produtos serão cadastrados? "))

# 2️⃣ Entrada dos códigos
codigos = input("Digite os códigos dos produtos separados por vírgula: ").split(',')

# Sanitize
codigos = [c.strip() for c in codigos]

# Validação
if len(codigos) != qtd:
    print("Quantidade de códigos diferente da quantidade informada.")
    exit()

# 3️⃣ Escreve os códigos
pyautogui.click(coord_codigo)
time.sleep(0.5)

for codigo in codigos:
    pyautogui.typewrite(codigo)
    pyautogui.press('enter')
    time.sleep(0.3)

# 4️⃣ Entrada das quantidades
quantidades = input("Digite a quantidade de cada produto, separadas por vírgula: ").split(',')
quantidades = [q.strip() for q in quantidades]

if len(quantidades) != qtd:
    print("Quantidade de itens diferente da quantidade informada.")
    exit()

# 5️⃣ Escreve as quantidades
pyautogui.click(coord_quantidade)
time.sleep(0.5)

for quantidade in quantidades:
    pyautogui.typewrite(quantidade)
    pyautogui.press('enter')
    time.sleep(0.3)

# 6️⃣ Entrada dos CPOs
cpos = input("Digite o CPO de cada produto, separados por vírgula: ").split(',')
cpos = [c.strip() for c in cpos]

if len(cpos) != qtd:
    print("Quantidade de CPOs diferente da quantidade informada.")
    exit()

# 7️⃣ Escreve os CPOs (com substituição)
pyautogui.click(coord_cpo)
time.sleep(0.5)

for cpo in cpos:
    valor_final = mapa_cpo.get(cpo, cpo)  # Substitui se estiver no mapa
    pyautogui.typewrite(valor_final)
    pyautogui.press('enter')
    time.sleep(0.3)

print("Cadastro concluído com sucesso!")
