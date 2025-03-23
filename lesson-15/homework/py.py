
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic Function")
plt.show()

x = np.linspace(0, 2*np.pi, 400)
plt.plot(x, np.sin(x), linestyle='-', color='r', marker='o', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='--', color='b', marker='s', label='cos(x)')
plt.legend()
plt.show()

fig, axs = plt.subplots(2, 2)
x = np.linspace(-2, 2, 400)
axs[0, 0].plot(x, x**3, 'r')
axs[0, 0].set_title("x^3")
axs[0, 1].plot(x, np.sin(x), 'g')
axs[0, 1].set_title("sin(x)")
x = np.linspace(0, 2, 400)
axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title("e^x")
axs[1, 1].plot(x, np.log(x+1), 'm')
axs[1, 1].set_title("log(x+1)")
plt.tight_layout()
plt.show()

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.scatter(x, y, c=np.random.rand(100), marker='o')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random Scatter Plot")
plt.grid()
plt.show()

data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
plt.title("3D Surface Plot")
plt.show()

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.bar(products, sales, color=['r', 'g', 'b', 'y', 'm'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.random.randint(10, 50, (3, 4))
plt.bar(time_periods, data[0], label=categories[0])
plt.bar(time_periods, data[1], bottom=data[0], label=categories[1])
plt.bar(time_periods, data[2], bottom=data[0]+data[1], label=categories[2])
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()
