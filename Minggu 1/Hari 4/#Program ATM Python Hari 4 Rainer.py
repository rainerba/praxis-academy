#Program ATM Python Hari 4 Rainer

class ATMMachine:
    def __init__(self, balance, deposit, withdraw):
        b = balance
        d = deposit
        w = withdraw
    def CheckBalance(self):
        print(f"Your Current Balance: {Balance.getBalance()}")

class Balance(ATMMachine):
    def getBalance(self):
        ATMMachine.CheckBalance()

class Deposit(ATMMachine):
    def setDeposit(self, d):
        ATMMachine.b += d
    def getDeposit(self):
        print(Deposit.setDeposit.d)

class Withdraw(ATMMachine):
    def setWithdraw(self, w):
        ATMMachine.b -= w
    def getWithdraw(self):
        print(Withdraw.setWithdraw.w)

ATMMachine.CheckBalance()