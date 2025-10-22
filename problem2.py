# find the factorial of a Given number
x=int(input("Enter a number:"))
f=1
for i in range(1,x+1):
    f=f*i
print("Factorial of",i,"is:",f)

 #Using math.factorial()Using math.factorial()
import math
x=int(input("Enter a number:"))
print(math.factorial(x))

