"""
Your module description
"""
print("Hello, welcome to NetworkChuck Coffee!!!!")
Name=input("what is your name?\n")

if Name=="Ben" or Name=="Pat"
    evilstatus=input("are you evil?")
    
    print("you're not welcome here\n")
    exit()
else:
    print("Hello " + Name + " Thank you for coming in today. \n" )

manu="black coffee, Espresso, Latte, Cappucino"

print (Name + ", what would you like to have? here's our manu\n" + manu)

order=input()
price=8
quantity=input("how many coffees would you like\n")
total=price*int(quantity)
print ("Thank you "+Name+ " your order of " + str(quantity) +" " + order + " your oder will be ready in 10 minutes, your total is " + str(total))

