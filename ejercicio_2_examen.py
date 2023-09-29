def divisible_entre_5(lista):
    return [True if i % 5 == 0 else False for i in lista]

lista = [10, 3, 5, 9, 15, 1]

d = divisible_entre_5(lista)
print(d)