import math
a=int(input("Digite o termo A: "))
b=int(input("Digite o termo B: "))
c=int(input("Digite o termo C: "))
Delta=b**2-4*a*c
print(f"O valor de delta é {Delta} ")
x1= (-b+ math.sqrt (Delta))/2*a
print("\n")
x2= (-b- math.sqrt(Delta))/2*a
print("\n")
print(f"O valor de x1= {x1}")
print("\n")
print(f"O valor de x1= {x2}")