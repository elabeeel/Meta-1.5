def repetidos(lista):
    elementos_unicos = set()
    conteo = {}

    for n in lista:
        if n not in elementos_unicos:
            elementos_unicos.add(n)
        else:
            if n in conteo:
                conteo[n] += 1
            else:
                conteo[n] = 2

    num_repetidos = sum(conteo.values())
    sin_repetir = len(lista) - num_repetidos
    tupla = (sin_repetir, num_repetidos)

    return tupla


l = [1, 3, 1, 4, 5, 3, 7]
r = repetidos(l)
print(r)

l2 = [1, 3, 1, 1, 3, 4]
r2 = repetidos(l2)
print(r2)