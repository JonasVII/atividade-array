import numpy as np

num = np.array([])
x = int(input("informe um valor de 0 a 7: "))
y = int(input("informe um valor de 0 a 7: "))

for i in range(8):
    numero = float(input("informe um número: "))
    num = np.append(num,numero)
soma = num[x]+num[y]
print(num,soma)