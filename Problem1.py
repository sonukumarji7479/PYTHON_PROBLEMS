#Bacis python problems
#1.Add two number
print("sum of two number")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
sum=x+y
print("sum of",x,"and",y,"is:",sum)

print("Sum of two number with function")
def sum(a,b):
    return a+b

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
x=sum(x,y)
print(x)

print("sum of two number using operator add")
import operator
print(operator.add(10,5))

#find maximam of two numbers in python
print("maximam of two mumber:")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("maximam value is:",max(x,y))

#find maximam of two numbers using if-eles statment
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
if x>y:
    print(x)
else:
    print(y)
    
# short() in python
a=[1,5,8,6,4,3,2,4,9,6,10]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# example of sort()
x=["apple","cherry","banana","grapss"]
x.sort()
print(x)


def add(x,y):
    return x+y
    
def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
    
def div(x,y):
    return x/y
    
print("1.Addition:")
print("2.Subtraction:")
print("3.Multiplication:")
print("4.Division:")
print("5.Exit")

choise=int(input("Enter your choise:(1,2,3,4,5):"))  
if choise in [1,2,3,4]:
    
     x=int(input("Enter fist number:"))
     y=int(input("Enter second number:"))

if choise==1:
      print("sum is",add(x,y))

elif choise==2:
    print("subtraction is:",sub(x,y))

elif choise==3:
    print("multiplication is:",mul(x,y))

elif choise==4:
    print("division is:",div(x,y))

elif choise==5:
    print("Exit thank you:")
    
else:
       print("invalid number")