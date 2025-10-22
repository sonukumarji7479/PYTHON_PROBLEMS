#find compound operator
p=float(input("Enter a principal input:"))
r=float(input("Enter of rate of iterest:"))
t=float(input("Enter a time:"))

a=p*(1+r/100)**t
ci=a-p
print(f"compound interest:{ci:.2f}")
print(f"total amount after interest:{a:.2f}")

