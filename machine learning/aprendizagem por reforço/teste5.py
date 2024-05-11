import numpy as np
from gym.spaces import Tuple, Box
estados = 1
test1 = np.zeros((3,3))
observation_space = Box(0, 2, shape=(3,), dtype=int), Box(0, 2, shape=(3,), dtype=int), Box(0, 2, shape=(3,), dtype=int)

test1 = test1.flatten()
test1Tupla = tuple(test1)

dicionario = {test1Tupla: [1, 2, 3, 5]}
print(dicionario)