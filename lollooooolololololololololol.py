Name = input("Enter your name: ")

print("Hi " + Name + " Welcome to the calculator where you can cheat in your Maths homework!")

a = input( int("Enter first number: "))
b = input( int("Enter second number: "))

op = input("Choose your operation (+,-,*,/) ")

if op == "+" :
    c = a + b
if op == "-" :
    c = a - b
if op == "*" :
    c = a * b
if op == "/" :
    c = a / b

print("Your answer is" , c)