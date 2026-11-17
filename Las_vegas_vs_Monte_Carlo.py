import random
import time

PI_REAL = 3.14159
r = 0.5  



def monte_carlo(N):
    inicio = time.perf_counter()
    dentro = 0
    for _ in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        if x * x + y * y < r * r:
            dentro += 1
    pi = 4 * (dentro / N)
    tiempo = time.perf_counter() - inicio
    return pi, abs(pi - PI_REAL), tiempo

def las_vegas(K):
    inicio = time.perf_counter()
    dentro = 0
    total = 0
    while dentro < K:
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        total += 1
        if x * x + y * y < r * r:
            dentro += 1
    pi = 4 * (dentro / total)
    tiempo = time.perf_counter() - inicio
    return pi, abs(pi - PI_REAL), tiempo, total


if __name__ == "__main__":
    random.seed(42)
    valores_N = [100, 1_000, 10_000, 100_000, 1_000_000]
    valores_K = [100, 1_000, 10_000, 100_000, 1_000_000]

    print("========== MONTE CARLO ==========")

    for N in valores_N:
        pi, diferencia, tiempo = monte_carlo(N)

        print("\nN:", N)
        print("PI estimado:", pi)
        print("Diferencia:", diferencia)
        print("Tiempo:", tiempo, "segundos")

    print("\n========== LAS VEGAS ==========")

    for K in valores_K:
        pi, diferencia, tiempo, total = las_vegas(K)

        print("\nK:", K)
        print("Puntos dentro:", K)
        print("Total generado:", total)
        print("PI estimado:", pi)
        print("Diferencia:", diferencia)
        print("Tiempo:", tiempo, "segundos")