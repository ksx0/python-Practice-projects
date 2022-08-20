# asking about the operatio


operation = input("would you like add/subtract/multiply/divide?:   ").lower()
if operation == "subtract" or operation == "divide":
    print("you chose {}".format(operation))
    print("keep in mind order of the number matters!")

num1 = input("What is your first number?: ")
num2 = input("What is your second number?: ")
num1,num2 = float(num1), float(num2)
#  setting up try and except

try:

    if operation == "add":
     result = num1+num2
     print("{} + {} = {}".format(num1,num2,result))
      
    elif operation == "subtract":
      result = num1-num2
      print("{} - {} = {}".format(num1,num2,result))

    elif operation == "multiply":
        result = num1*num2
        print("{} X {} = {}".format(num1,num2,result))
    
    elif operation == "divide":
        result = num1/num2
        print("{} / {} = {}".format(num1,num2,result))
    else:
        print("Sorry! {} is not an option".format(operation))
except: 
    print("Invalid entry")