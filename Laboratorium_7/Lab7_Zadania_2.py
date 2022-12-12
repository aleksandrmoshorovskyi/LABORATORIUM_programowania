import numpy as np

a = np.random.randint(low=0, high=50, size=(5, 5))

print(a)

print(f" max: {a.max()}, min: {a.min()} ")

print(f" max row: {a.max(axis=1)}, min col: {a.min(axis=0)} ")
