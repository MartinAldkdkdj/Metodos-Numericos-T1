from math import factorial
n=int(input("Digite valor de n: "))
x=int(input("Digite valor de x: "))
y=1
for i in range(n):
    i_s=i+1
    y=(x**i_s)/factorial(i_s)+y
z=1/y
print (y)
print (z)
