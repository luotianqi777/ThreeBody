import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import animation

size = 3
fig, axs = plt.subplots(1, 2)
location = np.random.rand(2, size) * 100
speed = (np.random.rand(2, size) - 0.5)
k = 10
axis_k = 0.3
ax = axs[0]
vx = axs[1]
ax.set_title('location')
line, = ax.plot(location[0, :], location[1, :], 'o')
vx.set_title('speed')
speed_line, = vx.plot(speed[0, :], speed[1, :], 'o')


def F(a, b):
    global k
    length = b - a
    theta = math.asin(length[1] / math.sqrt((length ** 2).sum()))
    f = min(k / (length ** 2).sum(), k / 10)
    res = np.asarray([f * math.cos(theta), f * math.sin(theta)])
    res = np.abs(res)
    res[np.where(length < 0)] *= -1
    return res


def speedChange():
    global location
    body = [location[:, i] for i in range(size)]
    f_body = np.zeros((2, size))
    for i in range(size):
        f_body[:, i] = np.asarray([F(body[i], body[j]) for j in range(size) if not j == i]).sum()
    return f_body


def animate(i):
    global speed, location
    speed += speedChange()
    location += speed
    line.set_xdata(location[0, :])
    line.set_ydata(location[1, :])
    step = location.ptp() * axis_k
    _min = location.min() - step
    _max = location.max() + step
    ax.axis([_min, _max, _min, _max])
    speed_line.set_xdata(speed[0, :])
    speed_line.set_ydata(speed[1, :])
    step = speed.ptp() * axis_k
    _min = speed.min() - step
    _max = speed.max() + step
    vx.axis([_min, _max, _min, _max])


ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, interval=20, blit=False)

plt.show()
