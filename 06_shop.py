import csv


class SaveCsv:
    def generate_header(self, no_rows):
        return [f"Column_{i}" for i in range(no_rows)]

    def save_data(self, save_dir: str,
                  data: list, mode: str = 'w') -> None:

        n_rows = len(data[0][0])
        header = self.generate_header(n_rows)

        with open(save_dir, mode) as f:
            writer = csv.writer(f)
            if mode == 'w':
                writer.writerow(header)
            writer.writerows(data)

    def read_data(self, save_dir):
        data = []
        try:
            with open(save_dir, 'r') as file:
                csvreader = csv.reader(file)
                next(csvreader)
                for row in csvreader:
                    data.append(row)
        except FileNotFoundError as err:
            print(err)
        return data


class MyShop(SaveCsv):
    def __init__(self,
                 shop_dir="shop.csv"):

        self.shop_dir = shop_dir
        self.shop = {}

    def read_shop_db(self):
        data = self.read_data(save_dir=self.shop_dir)
        for product, price in data:
            self.shop[product] = price

    def data_clean(self):
        self.shop.items()
        keys = self.shop.keys()
        val = self.shop.values()
        keys = list(map(lambda x: x.strip().lower(), keys))
        return list(zip(keys, val))

    def save_shop(self):
        data = self.data_clean()
        self.save_data(save_dir=self.shop_dir, data=data, mode='w')

    def show_products(self):
        for cargo, price in self.shop.items():
            print(f"Cena: {cargo} wynosi: {price}")

    def add_product(self, product: str, price: float):
        self.shop[product] = price
        self.save_data(save_dir=self.shop_dir, data=[[product, price]], mode='a')
        print("Produkt dodany")

    def del_product(self, product: str) -> None:
        deleted_prod = self.shop.pop(product, "Not found")
        print(deleted_prod)

    def change_product(self, product: str,
                       price: float) -> None:
        if product not in self.shop:
            print("Product nie istnieje!")
            dec = input("Czy chcesz zmienić product tak/nie: ")
            if dec == "tak":
                self.change_product()
            else:
                pass

        self.shop[product] = price

    def show_interface(self):
        action = ""
        while action != "Q":
            action = input("Co chesz zrobic: ")
            if action == "dodaj":
                self.add_product(product=input('Produkt: '),
                                 price=input('Cena: '))
            elif action == 'usun':
                self.del_product(product=input('Produkt: '))
            elif action == 'zmien':
                self.change_product(product=input('Produkt: '),
                                    price=input('Cena: '))
            elif action == 'wyswietl':
                self.show_products()
            elif action == 'zapisz':
                self.save_shop()
            elif action == 'Q':
                self.save_shop()


class Espresso:
    menu_type = 'Drink'

    def __init__(self):
        self.cup = 'hot'


if __name__ == "__main__":

    x = Espresso()
    y = Espresso()

    print(x.menu_type)
    print(y.menu_type)
    print(x.cup)
    print(y.cup)
    print()

    x.menu_type = 'Coffe'
    print(x.menu_type)
    print(y.menu_type)
    print()

    x.cup = 'cold'
    print(x.cup)
    print(y.cup)
    # s1 = MyShop("shop.csv")
    #
    # s1.read_shop_db()
    # s1.show_products()
    # s1.show_interface()

