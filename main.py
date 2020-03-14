from matplotlib import pyplot as plt
import numpy as np
import math

size = 3

fig, ax = plt.subplots()
location = np.random.rand(2, size) * 100
speed = (np.random.rand(2, size) - 0.5)
k = 5


def F(a, b):
    global k
    length = b - a
    theta = math.asin(length[1] / math.sqrt((length**2).sum()))
    FF = min(k / (length ** 2).sum(), k/10)
    res = np.asarray([FF * math.cos(theta), FF * math.sin(theta)])
    res = np.abs(res)
    res[np.where(length < 0)] *= -1
    return res


def speedChange():
    global location
    a = location[:, 0]
    b = location[:, 1]
    c = location[:, 2]
    fa = F(a, b) + F(a, c)
    fb = F(b, a) + F(b, c)
    fc = F(c, a) + F(c, b)
    res = np.asarray([fa, fb, fc]).T
    return res


count = 0
while count < 1000:
    count += 1
    speed += speedChange()
    location += speed
    plt.scatter(location[0, :], location[1, :])
    plt.savefig('res/' + str(count) + '.jpg')

