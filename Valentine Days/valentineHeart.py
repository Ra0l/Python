import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 15])
ax.axis('off')
ax.set_title("Feliz San Valentín", fontsize=14, fontweight='bold', color='red')

line, = ax.plot([], [], 'r', linewidth=3)
fill = ax.fill([], [], 'red', alpha=0.6)[0]


def init():
    line.set_data([], [])
    fill.set_xy(np.array([[], []]).T)
    return line, fill


def animate(i):
    scale = 1 + 0.1 * np.sin(2 * np.pi * i / 100)
    new_x = scale * x
    new_y = scale * y
    line.set_data(new_x, new_y)
    fill.set_xy(np.column_stack([new_x, new_y]))
    return line, fill


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=50, blit=True)
plt.show()
