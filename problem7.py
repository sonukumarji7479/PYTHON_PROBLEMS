# wrte a python script reverse a string without using built in function
string=input("Enter a string:")
rev=" "
for char in string:
    rev=char+rev
print("reverse string is",rev)