num = int(input("Enter number: "))
if (num > 100) or (num < 0):
    print("Invalid")
else:
    if (num == 2) or (num == 3) or (num == 5) or (num == 7) or (num == 9) or ((num % 2 !=0) and (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0) and (num % 9 != 0)):
        print("Prime number")
    else:
        print("not a prime number")


