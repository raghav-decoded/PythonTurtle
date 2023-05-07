# Input values
Int = int(input("Integer input : "))
Float = float(input("Float input : "))
String = str(input("String input :"))
default = (input("Default input : "))
# creating an empty list
a = []
# number of elements in a
n = int(input("Enter number of elements in the  : "))
# iterating till the range
for i in range(0,n):
    element = int(input())
    a.append(element) #adding the element
print(a)
print(Int)
print(Float)
print(String)
print(default)