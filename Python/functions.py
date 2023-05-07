# Functions
#Factorial calculator .
def ftrl(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print(f)    
n = int(input("Enter the number whose factorial has to be calculated : "))
ftrl(n)
