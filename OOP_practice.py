drinks_menu = {
    "1. Flat White": 3.40,
    "2. Filter Coffee": 2.80,
    "3. Iced Caramel Latte": 4.30,
    "4. Cold Brew": 3.50,
    "5. Hot Chocolate": 3.85,
    "6. Chai Latte": 3.90,
    "7. Matcha Latte": 4.20,
    "8. English Breakfast Tea": 2.60,
    "9. Peach Iced Tea": 3.75,
    "10. Coffee Frappé": 4.50
}


class Cart_item:
    def __init__(self,model,):
        self.model = model
        price = self.price
    
    

class Cart:
    def __init__(self,store,items):
        self.store = store
        self.items = items
        items = []    


    def shopping_cart_items(self):
        print(f"There are {len(self.items)} amount of items in the cart and they are; ",*self.items )

    


def exit_program():
    print("Thank you for using the program!")

    exit_button = input("Press the [ENTER] button to Exit the program: ")

    print("Exiting.....")

    quit()

    


def get_details():

    while True:

        try:
            drink_no = int(input("\nEnter Drink number:"))
        except ValueError:
            print("The drink number is invalid!.")
            continue

        if drink_no not in range(1,10):
            print("Your drink number is out of range!")

        elif drink_no == 1:
            print("Drink 1 has been added!")
       
        
        

    Shop.items.append(drink_no)



Shop = Cart("Lloyds Coffee",[])



def view_cart():
    
    print(f"\n{Shop.shopping_cart_items()}")



def remove_items():

     print(*Shop.items)

     while True:
            item_to_remove = input("\nEnter drink to remove:")
    
            if len(item_to_remove) < 1:
                print("Please enter a valid drink name!")
            elif item_to_remove.isdigit():
                print("The drink cannot be a number!")
            elif item_to_remove not in Shop.items:
                print("Drink entered is not in your cart!. Try again.")
            else:
                Shop.items.remove(item_to_remove)
                print(f"{item_to_remove} has succesfully been removed from your drink cart!.")
                view_cart()
                break
    

def drink_menu():
   
    print(f"Welcome to {Shop.store}!")

    print("="* 30)

    for drink, price in drinks_menu.items():
        print(f"{drink} costs £{price:.2f}")

    print("="* 30)

    get_details()
        

def main():
    flag = True

    print("#"*20)
    print("\n## 1. View drink menu")
    print("## 2. View added drinks")
    print("## 3. Checkout")
    print("## 4. Remove Items")
    print("## 5. Exit Program")
    print("")
    print("#"*20)

    while flag:
        try:
            choice = int(input("\nEnter a choice from the options above: "))
        except ValueError:
            print("Your choice Must be a number (1-4) ")
            continue

        if choice not in [1,2,3,4,5]:
            print("Invalid choice!.")

        elif choice == 1:
            drink_menu()

        elif choice == 2:
            view_cart()

        elif choice == 3:
            pass

        elif choice == 4:
            if len(Shop.items) == 0:
                print("\nThere is no drinks in your cart to remove!.")
            else:
                remove_items()
                continue
            
        elif choice == 5:
            exit_program()

        else:
            break

    

if __name__ == "__main__":
    main()
