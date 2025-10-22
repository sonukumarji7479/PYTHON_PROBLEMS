#1.find the factorial input given by user.
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
  fact=fact*i
print(fact)

#2.write a python script to print simple interest
p=int(input("Enter a principal input:"))
r=int(input("Enter of rate of iterest:"))
t=int(input("Enter a time:"))
si=p*r*t/100
print("simple interest is:",si)
total=si+p
print("total amount after interest:",total)

si=lambda p,r,t:(p*r*t)/100
p=int(input("Principal:"))
t=int(input("time:"))
r=int(input("rate:"))

res=si(p,t,r)
print(res)

#find compound operator
p=float(input("Enter a principal input:"))
r=float(input("Enter of rate of iterest:"))
t=float(input("Enter a time:"))

a=p*(1+r/100)**t
ci=a-p
print(f"compound interest:{ci:.2f}")
print(f"total amount after interest:{a:.2f}")


#sum of arrays
arr=[int(x) for x in input("Enter array sperated by dot:").split(".")]
t=sum(arr)
print("Arrays:",arr)
print("Total is:",t)

