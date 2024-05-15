import time


def cronometro(segundo):
    for x in range(segundo, 0, -1):
        print(f"Tempo restante: {x} segundo", end="\r")
        time.sleep(1)
    print("Tempo esgotado!")


segundo = int(input("Determine a quantidade de segundos que voce deseja: "))
cronometro(segundo)