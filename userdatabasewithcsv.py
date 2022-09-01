import csv
from IPython.display import clear_output
#importing important packages


# # handling user registration
def registerUser():
    with open("user.csv",mode="a",newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("Fill out the the given info.")
        userName = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        password2 = input("confirm password: ") #asking for data to write in CSV file
        clear_output()
        if password == password2:
            writer.writerow([userName,email,password])
            print("Registration successful!")
        else:
            print("something went wront. Try again!")


# # handling user login
def loginUser():
    print("To login please enter your info: ")
    userName = input("Username: ")
    email = input("email: ")
    password = input("password: ")
    clear_output()
    with open ("user.csv",mode="r") as f:
        reader = csv.reader(f, delimiter=",") #reading data from CSV file
        for row in reader:
            if row == [userName,email,password]: 
                print("Login succesful!")
                return True
    print("Try again!")
    return False
                

# main variable
logged_in = False
active = True
# main loop
while active == True:
    if logged_in:
        print("1. Logout \n2. Quit")
    else:
        print("1. Login \n2. Register \n3. quit")
        choice =  input("What do you want to do?: ").lower()
    clear_output()
    if choice == "login" and logged_in == False:
        loginUser()
        print("You are now logged in!")
    elif choice == "register" and logged_in == False:
        registerUser()
        print("You are successfully registered")
    elif  choice == "quit" and logged_in == False:
        active = False
        print("Thank you for using this program!")
    elif choice == "logout" and logged_in != False:
        logged_in = False
        print("You are now logged out!")
    elif choice == "quit" and logged_in != False:
        print("Try logging out first")
    else:
        print("Something went wrong! Try again...")


