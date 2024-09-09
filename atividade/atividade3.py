import numpy as np

num = np.array([])
pot = np.array([])
for i in range(10):
    numero = float(input("informe um número: "))
    num = np.append(num,numero)
pot = num**2
print(num)
print(pot)