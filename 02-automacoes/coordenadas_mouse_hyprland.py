import subprocess
import time

def obter_cursor():
    resultado = subprocess.run(
        ["hyprctl", "cursorpos"],
        capture_output=True,
        text=True
    )

    if resultado.returncode != 0:
        raise RuntimeError(resultado.stderr.strip())

    texto = resultado.stdout.strip()

    # Espera algo como "1234, 567"
    partes = texto.replace(",", " ").split()

    if len(partes) < 2:
        raise ValueError(f"Saída inesperada do hyprctl: {texto}")

    x = float(partes[0])
    y = float(partes[1])
    return x, y

print("Monitorando coordenadas do mouse no Hyprland...")
print("Pressione Ctrl + C para parar.\n")

try:
    while True:
        x, y = obter_cursor()
        print(f"\rX: {x} | Y: {y}   ", end="", flush=True)
        time.sleep(5)

except KeyboardInterrupt:
    print("\nPrograma encerrado.")
except Exception as e:
    print(f"\nErro: {e}")