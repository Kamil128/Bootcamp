import csv
#
# file = open("shop.csv")
# csvreader = csv.reader(file)
# header = next(csvreader)
# print(header)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
# file.close()
#
# import csv
# rows = []
# with open("shop.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)

data = [['pracownik_1', 3.5, 1000],
        ['pracownik_2', 2.6, 5000],
        ['pracownik_3', 1.8, 2000],
        ['pracownik_4', 6.5, 8000]]


def save_data(data_dir, data, mode):

    with open(data_dir, mode) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def read_data(data_dir):
    csv_data = []
    with open(data_dir, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_data.append(row)
    return csv_data


