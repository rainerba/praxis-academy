#Program ATM Python Hari 4 Rainer

class Balance:
    balance = 0.0
    def setBalance(self, b):
        self.balance = b
    def getBalance(self):
        return self.balance

class Deposit:
    deposit = 0.0
    def setDeposit(self, d):
        self.deposit = d
    def getDeposit(self):
        return self.deposit

class Withdraw:
    withdraw = 0.0
    def setWithdraw(self, w):
        self.withdraw = w
    def getWithdraw(self):
        return self.withdraw

class ATMMachine(Balance, Deposit, Withdraw):
    balance = Balance.getBalance()
    def CheckBalance(self):
        print(f"Your Current Balance: {Balance.getBalance()}")
    def withdraw(self):
        if(self.balance == 0):
            print("Your Current Balance is Zero")
            print("You Cannot Withdraw!")
            print("You Need to Deposit Money First.")
        elif(self.balance <= 500):
            print("You do not have sufficient money to withdraw")
            print("Check your balance to see your money in the bank.")
        elif(self.withdraw > self.balance):
            print("The amount you withdraw is greater than to your balance")
            print("Please check the amount you entered.")
        else:
            self.balance -= self.withdraw
            print(f"You withdraw the amount of {Withdraw.getWithdraw()} ")
    def depositMoney(self):
        print(f"You deposited the amount of {Deposit.getDeposit}")

print("Select ATM Transaction")
print("[1] Deposit")
print("[2] Withdraw")
print("[3] Balance Inquiry")
print("[4] Exit")
pilih = input()
while pilih < 4:
    x = pilih
    def menu(x):
        match x: 
            case "1":
                Deposit.deposit = input("Enter the amount of money to deposit: ")
                Balance.balance += Deposit.deposit
                ATMMachine.depositMoney()
            case "2":
                print("To withdraw, make sure that you have sufficient balance in your account.")
                Withdraw.withdraw = input("Enter amount of money to withdraw: ")
                ATMMachine.withdraw()
            case "3":
                ATMMachine.CheckBalance()
            case "4":
                print("Transaction exited.")


# x = ATMMachine()
# x.CheckBalance()
# x.setDeposit(20000)