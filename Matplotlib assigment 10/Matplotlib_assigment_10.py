import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-3, 3, 300)
y1 = np.linspace(-3, 3, 300)
x, y1 = np.meshgrid(x, y1)

f11 = x * y1
f12 = x**2 + y1**2
f13 = np.sin(3 * x) * y1

x_2d = np.linspace(-3, 3, 300)
f1 = x_2d**2
f2 = x_2d * np.sin(2 * x_2d)
f3 = np.arctan(x_2d)

fig = plt.figure(figsize=(15, 10))

# 3D Plots

# Plot f11
ax1 = fig.add_subplot(231, projection = '3d')
ax1.plot_surface(x, y1, f11, cmap = 'viridis')
ax1.set_title(r"$f_{11} = x \cdot y$", fontsize=12)

# Plot f12
ax2 = fig.add_subplot(232, projection = '3d')
ax2.plot_surface(x, y1, f12, cmap = 'plasma')
ax2.set_title(r"$f_{12} = x^2 + y^2$", fontsize=12)

# Plot f13
ax3 = fig.add_subplot(233, projection = '3d')
ax3.plot_surface(x, y1, f13, cmap = 'inferno')
ax3.set_title(r"$f_{13} = \sin(3x) \cdot y$", fontsize=12)

# 2D Plots

# Plot f1
ax4 = fig.add_subplot(234)
ax4.plot(x_2d, f1, color = "blue", linestyle = "-", marker="o", markersize = 2)
ax4.set_title(r"$f(x) = x^2$", fontsize = 12)
ax4.set_xlabel("x")
ax4.set_ylabel("f(x)")
ax4.axhline(0, color = "black", linewidth = 1, linestyle = "-")
ax4.axvline(0, color = "black", linewidth = 1, linestyle = "-")
ax4.grid(True, linestyle = "--", alpha = 0.6)

# Plot f2
ax5 = fig.add_subplot(235)
ax5.plot(x_2d, f2, color = "green", linestyle = "--", marker = "x", markersize = 2)
ax5.set_title(r"$f(x) = x \sin(2x)$", fontsize = 12)
ax5.set_xlabel("x")
ax5.set_ylabel("f(x)")
ax5.axhline(0, color = "black", linewidth = 1, linestyle = "-")
ax5.axvline(0, color = "black", linewidth = 1, linestyle = "-")
ax5.grid(True, linestyle="--", alpha=0.6)

# Plot f3
ax6 = fig.add_subplot(236)
ax6.plot(x_2d, f3, color = "red", linestyle = ":", marker = "^", markersize = 2)
ax6.set_title(r"$f(x) = \arctan(x)$", fontsize = 12)
ax6.set_xlabel("x")
ax6.set_ylabel("f(x)")
ax6.axhline(0, color = "black", linewidth = 1, linestyle = "-")
ax6.axvline(0, color = "black", linewidth = 1, linestyle = "-")
ax6.grid(True, linestyle = "--", alpha = 0.6)

plt.tight_layout()
plt.show()
