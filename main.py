from citeste_fisier import citeste_date_din_fisier
from cautare_aleatoare import cautare_aleatoare
from random_hill_climbing import random_hill_climbing


def main():
    numefisier = "rucsac-20.txt"  # Numele fișierului cu datele problemei
    obiecte, W = citeste_date_din_fisier(numefisier)
    k = 500  # Numarul de solutii generate aleator
    p = 10  # Numarul de vecini generati aleator

    def afisare_meniu():
        print("Meniu:")
        print("1. Random search")
        print("2. Random hill climbing")
        print("x. Exit")

    while True:
        afisare_meniu()
        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            cea_mai_buna_sol, cea_mai_buna_valoare, media_valori_valide, exec_time = cautare_aleatoare(obiecte, W, k)
            print("Cea mai bună soluție:", cea_mai_buna_sol)
            print("Valoarea cea mai bună:", cea_mai_buna_valoare)
            print("Media valorilor valide:", media_valori_valide)
            print("Timpul de execuție al programului:", exec_time, "secunde")
        elif optiune == "2":
            cea_mai_buna_sol, cea_mai_buna_valoare, media_valori_valide, exec_time = random_hill_climbing(obiecte, W, k, p)
            print("Cea mai bună soluție:", cea_mai_buna_sol)
            print("Valoarea cea mai bună:", cea_mai_buna_valoare)
            print("Media valorilor valide:", media_valori_valide)
            print("Timpul de execuție al programului:", exec_time, "secunde")
        elif optiune == "x":
            break
        else:
            print("Opțiune invalidă! Vă rugăm să selectați din nou.")


if __name__ == "__main__":
    main()
