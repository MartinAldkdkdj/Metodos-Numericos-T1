import math

def aproxe(x, n):
    
    if n == 0:
        return 1

    return math.pow(x, n) / math.factorial(n) + aproxe(x, n - 1)

x = int(input("Digita el valor de x: "))
n = int(input("Digita el valor de n: "))

suma= 1 / aproxe(x, n)

print("Resultado: ", suma)


