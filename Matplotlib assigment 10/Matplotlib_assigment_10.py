import random
import time
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

f1 = x**2
f2 = x * np.sin(2 * x)
f3 = np.arctan(x)

plt.figure(figsize = (10, 6))
plt.plot(x, f1, label = r"$f(x) = x^2$", color = "blue")
plt.plot(x, f2, label = r"$f(x) = x \sin(2x)$", color = "green")
plt.plot(x, f3, label = r"$f(x) = \arctan(x)$", color = "red")

plt.title("Graphs")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color = "black", linewidth = 1, linestyle = "-")
plt.axvline(0, color = "black", linewidth = 1, linestyle = "-")
plt.grid(True, linestyle = "--", alpha = 0.6)
plt.legend()

plt.show()