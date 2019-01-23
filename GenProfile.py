#!/usr/bin/env python3

import matplotlib.pyplot as plt

def cubicBezier(p_zero, p_one, p_two, p_three, t):
  x = (pow((1 - t), 3) * 3 * p_zero[0]) + (pow((1 - t), 2) * 3 * t * p_one[0]) + ((1 - t) * 3 * t * t * p_two[0]) + (t * t * t * p_three[0])
  y = (pow((1 - t), 3) * 3 * p_zero[1]) + (pow((1 - t), 2) * 3 * t * p_one[1]) + ((1 - t) * 3 * t * t * p_two[1]) + (t * t * t * p_three[1])
  print(str(x) + ' ' + str(y))
  return [x, y]

x_points = []
y_points = []

ticks = 10
time = 10

zero = [0, 0]
one = [float(time) * (3 / 4), 0]
two = [float(time) * (1 / 4), ticks]
three = [ticks, ticks]

for x in range(1000):
  final = cubicBezier(zero, one, two, three, float(x) / 1000)
  x_points.append(final[0])
  y_points.append(final[1])
#  print(final[0])
#  print(final[1])
  print('=======')

plt.plot(x_points, y_points)
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()
