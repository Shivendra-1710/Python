# a = input("Enter prompt to display to user")

# Make a calculator for multiplication of these two number by taking input from an user

a = int(input("Enter the first number: "))
b = float(input("Enter the second Number: "))

c = a * b

print(c)

# Check the class type 

print(type(a))
print(type(b))


# WAP to take marks of a user In English, Science and Maths and print he average of these marks.

English_marks = int(input("Enter the english's marks: "))    
Maths_marks = int(input("Enter the maths's marks: "))
Science_marks = int(input("Enter the science's marks: "))

Average_marks = (English_marks + Maths_marks + Science_marks) / 3
print(Average_marks)
 