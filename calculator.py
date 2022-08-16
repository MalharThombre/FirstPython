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