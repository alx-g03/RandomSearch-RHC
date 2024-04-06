import random
import time


def generare_sol_aleatoare(n):
    return [random.randint(0, 1) for _ in range(n)]


def validare_sol(sol, obiecte, W):
    greutate_totala = sum(sol[i] * obiecte[i][2] for i in range(len(sol)))
    return greutate_totala <= W


def calitate_sol(sol, obiecte):
    return sum(sol[i] * obiecte[i][1] for i in range(len(sol)))


def cautare_aleatoare(obiecte, W, k):
    cea_mai_buna_sol = None
    cea_mai_buna_valoare = float('-inf')
    valori_valide = []

    start_time = time.perf_counter()

    for _ in range(k):
        solutie = generare_sol_aleatoare(len(obiecte))
        if validare_sol(solutie, obiecte, W):
            valoare_sol = calitate_sol(solutie, obiecte)
            valori_valide.append(valoare_sol)
            if valoare_sol > cea_mai_buna_valoare:
                cea_mai_buna_sol = solutie
                cea_mai_buna_valoare = valoare_sol

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    media_valori_valide = sum(valori_valide) / len(valori_valide)

    return cea_mai_buna_sol, cea_mai_buna_valoare, media_valori_valide, exec_time
