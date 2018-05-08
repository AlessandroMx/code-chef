def factorial(num):
    if num == 1:
        return 1
    elif num > 1:
        return num * factorial(num - 1)

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        print(factorial(int(input())))