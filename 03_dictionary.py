# słownik = {klucz, wartość}

sklep = {"mleko": 5.0,
         "masło": 7.0,
         "lejsy": 5.5,
         }

print(sklep)
print(f"Cena mleka: {sklep['mleko']} PLN")
print(f"Cena masła: {sklep['masło']} PLN")

sklep["masło"] = 7.5
print(f"Cena masła: {sklep['masło']} PLN")

sklep['woda'] = 2.0
print(sklep)
print(f"Cena wody: {sklep['woda']} PLN")

for towar in sklep:
    print(f"Cena: {towar} wynosi: {sklep[towar]}")

for towar, cena in sklep.items():
    print(f"Cena: {towar} wynosi: {cena}")

# list_num.sort()
# sorted(list_num)

# list vs. tuple
list_num = [5, 1, 2, 3, 4]

tup_num = (1, 2, 3, 4)
print(list_num)
print(tup_num)

type(list_num)
type(tup_num)

list_num[2] = 5
print(list_num)

tup_num[2] = 5

dir(list_num)
dir(tup_num)

# Using a tuple instead of a list can give the programmer and the interpreter a hint that the data should not be changed.

ex = [('Swordfish', 'Dominic Sena', 2001),
      ('Snowden', ' Oliver Stone', 2016),
      ('Taxi Driver', 'Martin Scorsese', 1976)]

key_val = {('alpha','bravo'): 123}  # Valid
key_val = {['alpha','bravo']: 123}  # Invalid
