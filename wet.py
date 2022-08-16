print("Hi this is a program for dumb people who get wet in the rain.")
dum = input("Enter your name: ")
print("Hi mister " + dum + " this is the rain detector !")
rain = input("is it raining(y/n)")
umb = input("do you have an umbrella(y/n)")
if(rain == "y") and (umb == "n"):
    print("WET!")
if(rain == "n") and (umb == "y"):
    print("not wet")
if(rain == "n") and (umb == "n"):
    print("not wet")
if(rain == "y") and (umb == "y"):
    print("not wet\n NOW CLOSE THE COMPUTER IM TIRED CODING !!!!!!!!!!!!!")