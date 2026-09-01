class Account:
    def __init__(self,initial_balance):
        self.balance = initial_balance
        self.select_operation()
        
    def select_operation(self):
        op = int(input(
                "\nEnter the Operation you want to perform:"
                "\nFor debit enter 1"
                "\nFor credit enter 2"
                "\nTo show balance enter 3"
                "\nTo exit enter 4"
                "\n: "
            ))
        match op:
            case 1:
                amount = int(input("Enter amount to debit : "))
                self.debit(amount)
            case 2:
                amount = int(input("Enter amount to credit : "))
                self.credit(amount)
            case 3:
                self.get_balance()
            case 4:
                print("Thank you for using our banking system.")
                return
            case _:
                print("invalid input\n Enter Again")
                self.select_operation()
        
        
    def debit(self,amount):
        self.balance -= amount
        print(f'Rupees {amount} is debited from your account')
    
    def credit(self,amount):
        self.balance += amount
        print(f'Rupees {amount} is credited to your account')
    def get_balance(self):
        print("Your account Balance is ",self.balance)

acc1 = Account(10000)
