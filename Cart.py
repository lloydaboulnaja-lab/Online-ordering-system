class Cart:

    def __init__(self, items,cost):
        self.cost = []
        self.items = []

    def return_items(self):
        print(f"There are {len(self.items)} drinks in the cart which are: {self.items}")
        print(self.cost)

    def get_total(self):
        total = sum(self.cost)
        print(f"Your total to pay is ${total}.")

        pay = input("Press the [ENTER] button on the keybaord to pay: ")
        print("Payment went through succesfully!")
        
