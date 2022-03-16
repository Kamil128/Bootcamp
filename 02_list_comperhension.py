lista_imion = [
    "Kamil",
    "Gosia",
    "Paula",
    "Janusz"
]

lista_imion = lista_imion + ["Marek"]
lista_imion += ["Aneta"]
lista_imion.append("Monika")

print(lista_imion)
print(lista_imion[0])
print(lista_imion[3])
print(lista_imion[2:])
print(lista_imion[:3])
print(lista_imion[1:3])
print(lista_imion[-1])
print(lista_imion[-2])
print(lista_imion[:-2])
print(lista_imion[-2:])

for imie in lista_imion:
    print(imie)

len_lista_imion = len(lista_imion)
for i in range(len_lista_imion):
    print(lista_imion[i])


# Enumerate!!!
for n, imie in enumerate(lista_imion):
    print(f"Index {n}, Imie: {imie}")


# # list comprehension
lista_imion_c = []

for imie in lista_imion:
    imie_c = imie.upper()
    lista_imion_c.append(imie_c)

print(lista_imion_c)

lista_imion_c_c = [x.upper() for x in lista_imion]
print(lista_imion_c_c)


l1 = [x * x for x in range(0, 10, 3)]
print(l1)

l2 = [print(f"To jest liczba {x} a jej kwadrat to {x * x}") for x in range(10)]

l3 = [q * q for q in range(100) if not q % 7]
print(l3)

l4 = [q1 * q2 for q1 in range(1, 5) for q2 in range(99, 101)]
print(l4)

# ZIP()

# list unpacking
colors = ['red', 'blue', 'green']
colors = ['cyan', 'magenta', 'yellow', 'black']

a, *b, c, d = colors

# break
for i in range(10):
    for j in range(10):
        print(f"{i} {j}")
        if i == 5:
            break  # przerwie tylko loopa w środku
