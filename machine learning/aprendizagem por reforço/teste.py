import gymnasium as gym
import panda_gym
import time
env = gym.make("Taxi-v3", render_mode="rgb_array")
env.reset()

for _ in range(2):
    #image = env.render()  
    action = env.action_space.sample()
    observation, reward, terminated, trucated, info = env.step(action)
    if terminated or trucated: 
        env.reset()
time.sleep(2)

print(env.observation_space)
print(env.action_space)
env.close()