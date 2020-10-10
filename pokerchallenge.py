from itertools import permutations
from math import gcd

no_of_moves = 1
triangle = [2*i -1 for i in range(1,no_of_moves+1)]
#individaul movement
move = [i - no_of_moves for i in triangle if i > no_of_moves ]

def max_move(layer_of_candies):
    if layer_of_candies  is 1:
        return 0
    else:
        triangle = [2 * i - 1 for i in range(1, layer_of_candies + 1)]
        move = [i - layer_of_candies for i in triangle if i > layer_of_candies]
        return sum(move)

def find_group(lis):
    for value in permutations(lis):
        yield value

def find_gcd(value, b):
    prodcut = [i*i for i in value]

def find_product(values):
    product = 1
    for value in values:
        product *= value


for value in find_group([1,2,3]):
    print(value)

