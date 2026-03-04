import threading
from math import sqrt

def verificarPrimos(inicio, fim, resultados):
    for numero in range(inicio, fim):
        if numero < 2:
            continue
        
        if numero == 2:
            resultados.append(numero)
            continue
        
        if numero % 2 == 0:
            continue

        for i in range(3, int(sqrt(numero)) + 1, 2):
            if numero % i == 0:
                break
        else:
            resultados.append(numero)


def calcularPrimos():
    resultados = []
    threads = []

    n_threads = 4
    intervalo = 50000
    inicio_base = 10**6
    chunk = intervalo // n_threads

    for i in range(n_threads):
        inicio = inicio_base + i * chunk
        fim = inicio_base + (i + 1) * chunk

        t = threading.Thread(target=verificarPrimos, args=(inicio, fim, resultados))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Total de primos:", len(resultados))


if __name__ == "__main__":
    calcularPrimos()
