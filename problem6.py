# 1.write a python to check given number is prime or not          
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number:")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
