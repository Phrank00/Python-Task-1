class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self):
        print(f"How much will you like to deposit for {self.category}?\n")

    def withdraw(self):
        print(f"How much will you like to withdraw from {self.category}?\n")

    def balance(self):
        print(f"Your {self.category} balance is {self.amount}")

    def transfer(self):
        print(input(f"How much will you like to transfer for {self.category}?\n"))


category_1 = Budget("Food", 5000)
category_2 = Budget("Clothing", 15000)
category_3 = Budget("Entertainment", 4000)


category_1.transfer()