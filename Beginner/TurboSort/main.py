if __name__ == '__main__':
    numbers = []
    for i in range(int(input())):
        numbers.append(int(input()))
    numbers.sort()
    for num in numbers:
        print(num)