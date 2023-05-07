# String literals
string = "Raspberry Pi "
number = 3
print(string + str(number))
print(len(string)) #len() gives the string length.
print(string[0]) # Every character in the stringb has an idex number by which it can be accessed.
print(string[0:10]) # Seperation of idices with acolon to extract chunks of a string .
string = string.replace("Pi","Foundation") # replace() method replaces parts of a string and returns it .
print(string)
rawString = r"True\new" #raw string , \n not seen as escape character.
print(rawString)
print("Raspberry \n Pi \n Foundation")