import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self):
        self.state = np.random.rand()

    def update(self):
        self.state += np.random.randn()

num_agents = 10
timesteps = 100
runs = 5

plt.figure(figsize=(10, 6))

for run in range(runs):
    np.random.seed(run)
    agents = [Agent() for _ in range(num_agents)]
    for t in range(timesteps):
        for agent in agents:
            agent.update()
        states = [agent.state for agent in agents]
        plt.plot(states, label=f'Run {run+1}')

plt.xlabel('Time')
plt.ylabel('State of Agents')
plt.title(f'Agent-Based Model Simulation')
plt.show()
