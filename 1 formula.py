import math

def aproxe(x, n):
    
    if n == 0:
        return 1

    return math.pow(x, n) / math.factorial(n) + aproxe(x, n - 1)

x = int(input("Digita el valor de x: "))
n = int(input("Digita el valor de n: "))

suma = aproxe(x, n)

print("Resultado: ", suma)

# n = 10, x = -5, resultado =  0.86403
# n = 20, x = -5, resultado = 0.00674
# n = 30, x = -5, resultado = 0.00673
