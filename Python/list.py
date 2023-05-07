# List
array = [1,2,3,4]
print(str(array[2]) +"."+ str(array[0]) + str(array[3]))
a = input("List:")
list = a.split() # Splitting the characters in a 
print(a[0])
# creating an empty list
lst = []
# number of elements in a
n = int(input("Enter number of elements in the  : "))
# iterating till the range
for i in range(0,n):
    element = int(input())
    lst.append(element) #adding the element
print(lst)
