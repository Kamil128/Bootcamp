lista_imion = ["Kamil",
               "Gosia",
               "Paula"]

# dodawanie elementów
lista_imion = lista_imion + ["Marek"]
lista_imion += ['Aneta']
lista_imion.append("Monika")

print(lista_imion)

print(lista_imion[0])
print(lista_imion[1])
print(lista_imion[1:])
print(lista_imion[:3])
print(lista_imion[1:5])
# print(lista_imion[10])
print(lista_imion[:10])
print(lista_imion[-1])
print(lista_imion[-2])
print(lista_imion[-2:])
print(lista_imion[:-2])
print(lista_imion[:])

print(len(lista_imion))

for imie in lista_imion:
    print(imie)

for idx in range(len(lista_imion)):
    print(lista_imion[idx])

for r in range(5, 100, 42):
    print(r)

# i = 0
# for imie in lista_imion:
#     print(f"Index {i} imie: {imie}")
#     i += 1

for n, imie in enumerate(lista_imion):
    print(f"Index {n} imie: {imie}")

for n, imie in enumerate(range(10, 20, 3)):
    print(f"Index {n} imie: {imie}")

# list comprehension
lista_imion_c = []
for i in lista_imion:
    lista_imion_c.append(i.upper())

print(lista_imion_c)

lista_c = [ii.upper() for ii in lista_imion]
print(lista_c)

l1 = [x ** 2 for x in range(10)]
print(l1)
# KAMIL => User: KAMIL
l2 = [f"User: {k.upper()}" for k in lista_imion]
print(l2)

l3 = [x ** 2 for x in range(100) if x % 7 == 0]

# list unpacking
x = ["Kamil", "Pabijan", "Warszawa", "Polska"]
# i = x[0]
# n = x[1]
i, *other, n, m = x
print(f"{i} {n} {m}")
print(other)

x = [1, 2, 3]
t = (1, 2, 3)

x[1] = 4
print(x)