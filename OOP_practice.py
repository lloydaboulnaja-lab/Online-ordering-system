class Drink:

    def __init__(self,name,price):
        self.name = name
        self.price = price

        def get_name(self):
            return self.name

        def get_price(self):
            return self.price


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
        
cola = Drink("Coca Cola", 1.25)
fanta = Drink("Fanta", 1.20)
sprite = Drink("Sprite", 1.39)
drinks_cart = Cart([],[])

flag = True

print("1. Coca-Cola")
print("2. Fanta")
print("3. Sprite")
print("4. View drink cart")
print("5. Checkout")

while flag:

    try:
        choice = int(input("choose your drink: "))
    except ValueError:
        print("Invalid value!")
        continue
    if choice not in [1,2,3,4,5]:
        print("Invalid choice!. Try again")

    elif choice == 1:

        print(f"{cola.name} has been added to the cart!. It costs ${cola.price}!")
        drinks_cart.items.append(cola.name)
        drinks_cart.cost.append(cola.price)

    elif choice == 2:
        print(f"{fanta.name} has been added to the cart!. It costs ${fanta.price}!")
        drinks_cart.items.append(fanta.name)
        drinks_cart.cost.append(fanta.price)

    elif choice == 3:
        print(f"{sprite.name} has been added to the cart!. It costs ${sprite.price}!")
        drinks_cart.items.append(sprite.name)
        drinks_cart.cost.append(sprite.price)
        
    elif choice == 4:
        if len(drinks_cart.items) < 1:
            print("You dont have any drinks in your cart!")
            continue
        else:
            drinks_cart.return_items()

    elif choice == 5:
        if len(drinks_cart.items) < 1:
            print("You dont have any drinks in your cart!")
            continue
    
        else:
            drinks_cart.get_total()

            after_choice = input("\nDo you wish to \n  1. Continue \n  2. Exit: ")

            if after_choice == 2:
                quit()     
            else:
                continue
