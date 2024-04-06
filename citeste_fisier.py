def citeste_date_din_fisier(numefisier):
    with open(numefisier, 'r') as f:
        linii = f.readlines()

    obiecte = []
    for linie in linii[1:-1]:
        numar, valoare, greutate = map(int, linie.strip().split())
        obiecte.append((numar, valoare, greutate))

    W = int(linii[-1])

    return obiecte, W
