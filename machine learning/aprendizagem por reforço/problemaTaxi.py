import random
import gym
import time

env = gym.make('Taxi-v3', render_mode="rgb_array")
env.reset()
env.render()

print(env.action_space)
print(env.observation_space)
print(env.P)

