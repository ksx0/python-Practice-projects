#importing functions
from IPython.display import clear_output
#global variable
cart = []

#functions needed
#add to the list
def addItem(item):
    clear_output()
    cart.append(item)
    print("{} is added to the cart".format(item))

# removing from the list

def removeItem(item):
    clear_output()
    cart.remove(item)
    print("{} is removed to the cart".format(item))

#clearing the list

def clearItem():
    clear_output()
    cart.clear()
    print("Cart is empty")

# showing the items

def showItem():
    if cart:
        print("Here is your cart :")
        for item in cart:
            print("- {}".format(item))
    else:
        print("your cart is empty")

#main function

def main():
     done = False
     while not done:
        ans = input("How may I help you? select: add/remove/clear/show/quit: ").lower()
        if ans == "quit":  #case one
            showItem()
            print("Thank you for using our app.")
            done = True
        elif ans == "add":  #case two
            item = input("Add to list:  ").title()
            addItem(item)
        elif ans == "remove": #case three
           item = input("remove item:  ").title()
           removeItem(item)
        elif ans =="clear": #case four
            clearItem()
        elif ans == "show": #case five
            showItem()
        else:
            print("Its not a valid option - Try again!")

main()