def check_round_winner(a, b):
    if a - b > 0:
        return (1, a - b)
    else:
        return (2, b - a)


if __name__ == '__main__':
    (winner, lead) = (0, 0)
    for i in range(int(input())):
        (a, b) = map(int, input().split(' '))
        (tmp_winner, tmp_lead) = check_round_winner(a, b)
        if tmp_lead > lead:
            (winner, lead) = (tmp_winner, tmp_lead)
    print(winner, lead)
