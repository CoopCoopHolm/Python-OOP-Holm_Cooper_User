class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self, amount):
        self.account_balance == amount
    
coopcoopholm = User("Cooper Holm", "coop.coop@coop.com")
jodoe = User("Joe Doe", "joe@joe.com")
goobypls = User("Gooby Please", "gooby@please.com")

coopcoopholm.make_deposit(34869500)
coopcoopholm.make_deposit(5982870)
coopcoopholm.make_deposit(12078500)
coopcoopholm.make_withdrawal(801980)
coopcoopholm.display_user_balance
print(coopcoopholm.account_balance)

jodoe.make_deposit(1593841)
jodoe.make_deposit(25483157)
jodoe.make_withdrawal(11687)
jodoe.make_withdrawal(332520)
jodoe.display_user_balance
print(jodoe.account_balance)

goobypls.make_deposit(20)
goobypls.make_withdrawal(5)
goobypls.make_withdrawal(5)
goobypls.make_withdrawal(5)
goobypls.display_user_balance
print(goobypls.account_balance)