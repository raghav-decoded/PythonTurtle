# The key value method  
year = int(input("Enter the year : "))
month = input("Enter the month : ")
day = int(input("Enter the day : "))
last = year % 100  # last two digits of the year
last = int(last/4)  # divide by 4 and drop the remainder
last = last + day  # add the day number

# Adding the month's key value
month = month.lower()  # Converting the string to lowercase 
if month == "january" or month == "october" :
    last = last + 1
elif month == "february" or month == "march" or month == "november" :
    last = last + 4
elif month == "april" or month == "july" :
    last = last + 0
elif month == "may" :
    last = last + 2
elif month == "june" :
    last = last + 5
elif month == "august" :
    last = last + 3
elif month == "september" or month == "december" :
    last = last + 6

# if january or february of a leap year subarct 1.
if month == "january" and year % 4 == 0 :
    last = last - 1
elif month == "february" and year % 4 == 0 :
    last = last - 1
    
# gregorian calender repeats every 400 years
while(year > 2100 or year < 1700):
    year = year - 400
    
# adding the century code
if year >= 1700 and year < 1800 :
    last = last + 4
elif year >= 1800 and year < 1900 :
    last = last + 2
elif year >= 1900 and year < 2000 :
    last = last + 0
elif year >= 2000 and year < 2100 :
    last = last + 6

last = last + year % 100  # adding the last two digits of the year
last = last % 7  # divide by 7 and take the remainder

week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
print("The day is " + week[last] + " for the given date." )