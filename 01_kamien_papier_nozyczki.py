import random

print("Hello")
print("Zagrajmy w gre!")

# TODO: Dodać listę uczestkików

game = ["kamien", "papier", "nozyczki"]
score = 0


def wygrales(score):
    print("Wygrałaś/eś")
    return score + 1


# TODO: Wybrać/Ograniczyć ilość rund
while True:
    random_number = random.randint(0, 2)
    computer_input = game[random_number]
    user_input = input("Wybierz kamien/papier/nozyczki, Q aby wyjść: ")

    if user_input == "Q":
        break

    user_input = user_input.lower()
    if user_input not in game:
        print("Wybierz jeszcze raz!")
        continue

    print("Komputer wybrał " + computer_input)
    print("Gracz wybrał " + user_input)

    cond = [user_input == "papier" and computer_input == "kamien",
            user_input == "kamien" and computer_input == "nozyczki",
            user_input == "nozyczki" and computer_input == "papier"]

    if any(cond):
        score = wygrales(score)
    elif user_input == computer_input:
        print("Remis!")
    else:
        print("Przegrałeś/aś")
        score -= 1

    # TODO: Wypisać podsumowanie/Statystyki
    print(f"Twoje punkty: {score}")
