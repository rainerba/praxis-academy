#Program ATM Python Hari 4 Rainer
balance = 0.0
withdraw = 0.0
deposit = 0.0

p = input("Insert PIN: ")

class ATMMachine:
    def __init__(self, pin):
        self.pin = pin
    def CheckBalance(self):
        print("Your Current Balance is: {}".format(Balance(p, balance).getBalance()))
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
        print("You deposited the amount of {}".format(x.getDeposit()))

class Balance(ATMMachine):
    def __init__(self, pin, balance):
        ATMMachine.__init__(self, pin)
        self.balance = balance
    def getBalance(self):
        return self.balance

class Deposit(ATMMachine):
    def __init__(self, pin, deposit):
        ATMMachine.__init__(self, pin)
        self.deposit = deposit
    def getDeposit(self):
        return self.deposit

class Withdraw(ATMMachine):
    def __init__(self, pin, withdraw):
        ATMMachine.__init__(self, pin)
        self.withdraw = withdraw
    def getWithdraw(self):
        return self.withdraw

pilih = 0
while True:
    print("Select ATM Transaction")
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Balance Inquiry")
    print("[4] Exit")
    pilih = input("Select Transaction: ")
    if(pilih == "1"):
        x = Deposit(p, float(input("Enter the amount of money to deposit: ")))
        Balance(p, balance).balance = Deposit(p, deposit).getDeposit()
        ATMMachine(p).depositMoney()
        Balance(p, balance).getBalance()
    elif(pilih == "2"):
        print("To withdraw, make sure that you have sufficient balance in your account.")
        ATMMachine(p).Withdraw(p, float(input("Enter amount of money to withdraw: ")))
        ATMMachine(p).withdraw()
    elif(pilih == "3"):
        ATMMachine(p).CheckBalance()
    elif(pilih == "4"):
        print("Transaction exited.")
        break
    else:
        print("Error Input! Please enter a correct number only.")