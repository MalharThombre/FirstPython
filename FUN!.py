name = input("Enter your name: ")
print("Hi " + name + " this is the calculator! Using this you can cheat IN YOUR MATHS HOMEWORK! Then what are you waiting for? let's get started ")
a = int(input("enter first number: "))
b = int(input("enter second number: "))
op = input("choose an operation: ")
if op == "+" :
    c = a + b
if op == "-" :
    c = a - b
if op == "*" :
    c = a * b
if op == "/" :
    c = a / b
print("Answer" , c)
print("Hope you enjoyed" + name)

