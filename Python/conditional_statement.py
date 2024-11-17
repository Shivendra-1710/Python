# if 
# if test expression:
    # statement(s)

# the body of if is executed only if test expression is true

# example

age = int(input("plz enter your age for entry: "))

if age > 24:
    print("You can go to club")         
print("This line will always be executed")


# if else
# if test expression:
#     Body of if
# else:
#     Body of else 

# if the condition is false, body of else is executed. Indentation is used to seperate the block 

# example

if age >= 18:
    print("you can go to club!")
else:
    print("Sorry you can't go to club, be mature first!")

# if..elif..else

# if test expression:
#     Body of if
# elif test expression:
#     Body of elif
# else:
#     Body of else

# example

num = float(input("Enter any number to check whether it is positive, negative & zero: "))

if num > 0:
    print("Positve Number!")
elif num == 0:
    print("Zero!")
else:
    print("Negative Number!")