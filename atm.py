class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
    def check_balance(self):
        print("Money Remainig")
        print("Money = 10000")
    def withdrawl1(self,money):
        new_amount = 10000 - money
        print("You took "+str(money) + ". Your have "+ str(new_amount))
def main():
    print("Sup Dude Welcome ")
    Account = input(" Enter your acount number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")
    new_user =  Atm(Account,Card_number,pin_number)
    print("Choose your activity ")
    print("1.Balance Check  2.Withdrawl")
    activity = int(input("What To Do?? "))
    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("Withdraw")
        money = int(input("Take Money "))
        new_user.withdrawl1(money)
        print('Thank you ')
if __name__ == "__main__":
    main()