CONS = {
    0: 1,
    1: 2,
    2: 4,
    3: 8,
    4: 16,
    5: 32,
    6: 64,
    7: 128,
    8: 256,
    9: 512,
    10: 1024,
    11: 2048
}

def get_nearest_constant(num):
    distance = 100000
    val = num
    for key, value in CONS.items():
        tmp_dist = num - value
        if tmp_dist <= distance and tmp_dist >= 0:
            distance = tmp_dist
            val = value
        else:
            break
    return val

def get_combinations(num, result=[]):
    if num > 0:
        tmp_num = get_nearest_constant(num)
        result.append(tmp_num)
        get_combinations(num - tmp_num, result)
    return result

if __name__ == '__main__':
    for i in range(int(input())):
        num = int(input())
        res = get_combinations(num)
        print(len(res))
        del res[:]