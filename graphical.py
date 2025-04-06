import numpy as np
import matplotlib.pyplot as plt

def plot_equations():
    x = np.linspace(-10, 10, 400)
    y1 = (3 - x)
    y2 = x - 1
    plt.plot(x, y1, label='x + y = 3', color='blue', linewidth=2)
    plt.plot(x, y2, label='x - y = 1', color='red', linewidth=2)
    plt.axhline(0, color='black', linewidth=0.8)  
    plt.axvline(0, color='black', linewidth=0.8)  
    plt.xlabel("x-axis")  
    plt.ylabel("y-axis")  
    plt.title("Graph of Two Linear Equations")  
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

plot_equations()