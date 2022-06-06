# Indexación de matrices
import numpy as np

a = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
)

print(a)
b = a[:2,1:3]

print('\n', b)

c = a[1:3,:2]
print('\n',c)

# voltear entrada en cada fila
d = np.fliplr(a)
print(d)

print(d[2,1])

d = np.flip(a)
print(d)

