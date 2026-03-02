from my_thread import MyThread
import time
from math import sqrt
import threading


def verificarPrimo(numero):
    if numero < 2:
        print(f"Número {numero} não é primo")
        return False
    
    if numero == 2:
        print(f"Número {numero} É primo")
        return numero
    
    if numero % 2 == 0:
        print(f"Número {numero} não é primo")
        return False

    limit = int(sqrt(numero)) + 1
    for i in range (3, limit, 2):
        if numero % i == 0:
            print(f"Número {numero} não é primo")
            return False
    
    print(f"Número {numero} É primo")
    return numero 


def calcularPrimos():
    threads = []
    for i in range (10, 21):
        t = threading.Thread(target=verificarPrimo, args=(i,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    calcularPrimos()