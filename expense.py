class Expense:

    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def display(self):
        print(
            self.name,
            "- ₹",
            self.amount,
            "-",
            self.category
        )

    def update(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.name} - ₹ {self.amount} - {self.category}"