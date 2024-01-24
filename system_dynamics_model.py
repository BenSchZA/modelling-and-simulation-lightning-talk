import numpy as np
import matplotlib.pyplot as plt

timesteps = 100
runs = 5

plt.figure(figsize=(10, 6))

for run in range(runs):
    np.random.seed(run)
    x = 0
    results = []
    for _ in range(timesteps):
        x += np.random.randn()  # Random influence
        results.append(x)
    plt.plot(results, label=f'Run {run+1}')

plt.xlabel('Time')
plt.ylabel('Value of x')
plt.title('System Dynamics Simulation')
plt.legend()
plt.show()
