# Check if palindrome

# A string can be a palindrome only if it has even pair of characters and at max 1 odd character

# asdfgfdsa

# {'a': 2, 'g': 1}

def palindrom_checker(text):
    text = text.lower()
    lista_lister = {}
    parzyste_litery = 0
    nieparzyste_litery = 0

    for i in text:
        if i in lista_lister.keys():
            lista_lister[i] += 1
        else:
            lista_lister[i] = 1

    for litera in lista_lister:
        if lista_lister[litera] % 2 == 0:
            parzyste_litery += 1
        else:
            nieparzyste_litery += 1

    if (nieparzyste_litery > 1) or (parzyste_litery == 0):
        return False
    else:
        return True


print(palindrom_checker("carerac"))
print(palindrom_checker("A"))



