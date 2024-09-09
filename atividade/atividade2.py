import numpy as np

num = np.array([])

for i in range(6):
    numero = int(input("informe um número: "))
    num = np.append(num,numero)
print(num)