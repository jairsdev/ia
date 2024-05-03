import random
import gymnasium as gym
import numpy as np
from IPython.display import clear_output
import panda_gym
import time

env = gym.make("Taxi-v3", render_mode="ansi")
qTabela = np.zeros([env.observation_space.n, env.action_space.n])
probabilidade = 0.1
gamma = 0.6
alpha = 0.1

for i in range(10000):
    estado = env.reset()[0]
    recompensa, penalidade = 0, 0
    encerrado, truncado = False, False

    while not encerrado and not truncado:
        if (random.uniform(0, 1) < probabilidade):
            acao = env.action_space.sample()
        else:
            acao = np.argmax(qTabela[estado])
        
        proximoEstado, recompensa, encerrado, truncado, info = env.step(acao)

        qAntigo = qTabela[estado, acao]
        qProximo = np.max(qTabela[proximoEstado])
        qNovo = (1 - alpha) * qAntigo + alpha * (recompensa + gamma * qProximo)
        qTabela[estado, acao] = qNovo

        if recompensa == -10:
            penalidade += 1
        
        estado = proximoEstado
    if i % 100 == 0:
        clear_output(wait=True)
        print('Episódio: ', i)

print("Treinamento concluído")

episodios = 50
totalPenalidades = 0
frames = []

for _ in range(episodios):
    estado = env.reset()[0]
    recompensa = 0
    encerrado, truncado = False, False

    while not encerrado and not truncado:
        acao = np.argmax(qTabela[estado])
        estado, recompensa, encerrado, truncado, info = env.step(acao)

        if recompensa == -10:
            totalPenalidades += 1
        
        frames.append({
            'frame': env.render(),
            'action': acao,
            'state': estado,
            'reward': recompensa
        })

print(episodios)
print(totalPenalidades)

env.close()
for frame in frames:
    print(frame['frame'])
    print(frame['action'])
    print(frame['state'])
    print(frame['reward'])
