# Write a function that takes in a list of dictionaries with a key and list of
# integers and returns a dictionary with the standard deviation of each list.
#
# Note that this should be done without using the numpy built in functions.

# output -> {'list1': val, 'list2': val

from math import sqrt  # hint

input = [
    {
        'index': 'S&P',
        'price': [4207.31, 4210.27, 4198.55, 4201.33, 4200.43, 4199.99],
    },
    {
        'index': 'Dow Jones ',
        'price': [32944.19, 32935.20, 33937.44, 32994.12, 32940.99, 32945.75, 32946.98],
    }
]


# ############################################
# ################  Solution  ################
# ############################################

def mean(l):
    return sum(l)/len(l)


def std(lt):
    mean_val = mean(lt)
    return sqrt(mean([(x - mean_val)**2 for x in lt]))



output = {x['index']: std(x['price']) for x in input}
print(output)
