age = 70

if age < 4:
    price = 0
elif age <18:
    price = 5
elif age <64:
    price = 12
elif age >64:
    price = 3
else:
    price = 10
print ("De toegangsprijs is $" + str(price) +",-" + " want je leeftijd is " + str(age) +", oud hoor!")
