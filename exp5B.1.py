#string using third variable
a=str(input("Enter the string value a:"))
b=str(input("Enter the string value b:"))
temp=a
a=b
b=temp
print("After swaping")
print("Value of a:",a)
print("value of b:",b)