import numpy as np

#a)
num = np.array([1,0,5,-2,-5,7])#1,0,5,-2,-5,7

for i in range(6):
    numero = int(input("informe um número: "))
    num = np.append(num,numero)
    print(num[i])
print(num)

#b)
soma = num[0]+num[1]+num[5]
print(soma)

#c)
num[4] = 100
print(num)


