from functools import reduce

if __name__ == '__main__':
    for i in range(int(input())):
        print(reduce(lambda x, y : x + y, map(int, list(input()))))