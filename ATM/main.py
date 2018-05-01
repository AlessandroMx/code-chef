class Account(object):
    '''
    Simple class to represent a bank account and some movements it can execute
    '''

    def __init__(self, balance):
        self.balance = float(balance)

    def withdraw(self, amount):
        amount = int(amount)
        self.balance = self.balance - amount - 0.5 if amount % 5 == 0 and amount + \
            0.5 <= self.balance else self.balance


if __name__ == '__main__':
    data = input().split(' ')
    account = Account(data[1])
    account.withdraw(data[0])
    print('{0:.2f}'.format(account.balance))
