from itertools import takewhile

class HasSum(Exception): pass

def sumOfDividers(candidate):
    sqrt = candidate**0.5
    list = ((n, candidate/n) for n in xrange(2, int(sqrt) + 1)
            if not candidate%n)
    list = [item for tuple in list for item in tuple]
    list.append(1)
    return sum(set(list))

def abundants(limit):
    collection, logical = [], (limit + 1) * [False]
    for n in range(1, limit + 2):
        if sumOfDividers(n) > n:
            logical[n] = True
            collection.append(n)
    return collection, logical

def main():
    limit, result = 28123, 0
    collection, logical = abundants(limit)
    for number in range(1, limit + 1):
        try:
            for first in takewhile(lambda x: x <= number/2, collection):
                if logical[number - first]: raise HasSum
        except HasSum: pass
        else: result += number
    return result

if __name__ == '__main__':
    print main()