# product name & price
from email import message


p1, p1_price = "books",7.00
p2, p2_price = "Laptop", 100.00
p3, p3_price = "Desk", 254.80

# company information
company_name = "Coding Template, Inc."
company_address = "283 Franklin st."
company_city ="Bosto, MA"

# declaring end message
message = "Thank you for shopping with us" 



# creating top border
print("*" * 50)
# company info
p1, p1_price = "Books", 7.00
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# creating divide
print("="*50)

# printing bill
print("\tproduct name \tprice".upper())
print("\t{}\t\t${}".format(p1.title(),p1_price))
print("\t{}\t\t${}".format(p2.title(),p2_price))
print("\t{}\t\t${}".format(p3.title(),p3_price))

print("="*50)
# calculating total
total  = p1_price+p2_price+p3_price
print("\t\t\tTotal\n\t\t\t{}".format(total))

print("="*50)
# printing message

print("\t{}!".format(message))

print("*"*50)

