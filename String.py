name = "ragnAr loThbrok"
print(name)
#title() displays each word in titlecase, where each word begins with a capital letter.
print(name.title())
#upper() display each word of string to uppercase letters
print(name.upper())
#lower() display each word of string to lowercase letters
print(name.lower())
fname = "Ragnar"
lname = "Lothbrok"
#Python uses the plus symbol ( + ) to combine strings is called concatenation.
fullname = fname+" "+lname
print("King "+fullname)
fname = " Ragnar "
#To remove whitespace exists at the right end of a string, use the rstrip() method.
print(fname.rstrip())
#To remove whitespace exists at the left end of a string, use the lstrip() method.
print(fname.lstrip())
#To remove whitespace exists at both the end of a string, use the strip() method.
print(fname.strip())
#The apostrophe appears inside a set of double quotes
var = "Don't worry"
print(var)
age = 22
#str() function tells Python to represent non-string values as strings
message = 'happy '+ str(age) +'nd birthday'
print(message)
