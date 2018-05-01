if __name__ == '__main__':
    config_data = input().split(' ')
    times = int(config_data[0])
    num = int(config_data[1])
    res = 0
    for i in range(times):
        res += 1 if int(input()) % num == 0 else 0
    print(res)