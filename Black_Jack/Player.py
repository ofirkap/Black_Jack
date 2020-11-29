class Player:

    def __init__ (self):

        self.name = input('Please enter your name here: ')
        self.bank = int(input('How much would you like to play for?: '))
    
    def __str__(self):
        return f"name: {self.name} balance: {self.bank}$"
    
    def bet(self):
        amount = int(input("How much would you like to bet in this round?"))
        while (self.bank < amount):
            print("You don't have enough money to make that bet")
            amount = int(input("How much would you like to bet in this round?"))
        self.bank -= amount
        print(f"You have successfully placed a bet of {amount}$")
        return amount
    
    def add_funds(self, amount):
        self.bank += amount