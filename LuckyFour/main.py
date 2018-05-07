if __name__ == '__main__':
    for i in range(int(input())):
        print(len(list(filter(lambda x: x == 4, map(int, list(input()))))))