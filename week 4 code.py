import math

for a in range(11):
    a=a+1
    print(float(1/a))

math.sqrt(4)

def bs (a, b, c):
    bighood =  (b**2) - (4*a*c)
    topfirst = -b + math.sqrt(bighood)
    topsecond =-b - math.sqrt(bighood)
    ansone= topfirst/2*a
    anstwo= topsecond/2*a
    print("Root 1:",float(anstwo),"\nRoot 2:",float(ansone))

x=1
y=-5.86
z= 8.5408
bs(x,y,z)


