if __name__ == '__main__':
    for i in range(int(input())):
        nums = list(map(int, list(input())))
        print(nums[0] + nums[-1])