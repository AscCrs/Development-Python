from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

from matplotlib.font_manager import FontProperties

# Se usa para resolver el problema de mostrar fuentes chinas en el sistema Windows
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=45)

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

[x, t] = np.meshgrid(
    np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi
)
p = np.pi / 2 * np.exp(-t / (8 * np.pi))
u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x**2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))

# Tonos amarillentos a oscuros   YlOrBr
# Tonos calidos gist_heat
# Tono autumn
surf = ax.plot_surface(
    r * np.cos(t),
    r * np.sin(t),
    u * (x * np.cos(p) - y * np.sin(p)),
    rstride=10,
    cstride=10**10,
    cmap=cm.Wistia,
    linewidth=7,
    antialiased=True,
)

plt.title("I Love You! ", fontproperties=font)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.show()
