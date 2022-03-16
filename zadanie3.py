# You have store credit of N dollars. However, you don’t want to walk a long distance with heavy books, but you want to spend all of your store credit.

# Let’s say we have a list of books in the format of tuples where the first value is the price and the second value is the weight of the book -> (price,weight).

# Write a function optimal_books to retrieve the combination allows you to spend all of your store credit while getting at least two books at the lowest weight.

# Note: you should spend all your credit and getting at least 2 books, If no such condition satisfied just return empty list.

# Example:

# N = 18
# books = [(17,8), (9,4), (18,5), (11,9), (1,2), (13,7), (7,5), (3,6), (10,8)]

# def optimal_books(N, books) -> [(17,8),(1,2)]

# Solution

import itertools


def optimal_books(N, books):
    print("(Price,Weight) details of books: ", books)
    print("Store Credit: ", N)
    final_books = []  # empty list to store the final books
    # sorting the books by weight as we need the lightest books
    sorted_books = sorted(books, key=lambda x: x[1])
    price = [i[0] for i in sorted_books]  # list of prices sorted by weight

    for i in range(2, len(price) + 1):
        templist = (list(itertools.combinations(price, i)))  # generating all combinations of price
        res = [sum(j) for j in templist]  # summing individual combination to get total price of each combination
        if N in res:  # if the result matches traceback traceback and append the combination
            tempbooks = (templist[res.index(N)])
            for k in tempbooks:
                final_books.append(sorted_books[price.index(k)])
            break

    return final_books


N = 18
books = [(17, 8), (9, 4), (18, 5), (11, 9), (1, 2), (1, 3), (13, 7), (7, 5), (3, 6), (10, 8)]
print("Best Combination: ", optimal_books(N, books))





