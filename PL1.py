# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

#calculate the mean of the data
def cummean(arr):
 return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=float)

#use the mean to calculate the std
def cumstd(arr):
 return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2)

# declaring variables

circle_x = np.linspace(0, 1, 100)
circle_y = np.sqrt(1-circle_x**2)

times = 1000000

x = np.random.rand(times)
y = np.random.rand(times)

# plot graph with random points

fig2 = plt.figure()

fig2.set_size_inches(5, 5)

plt.plot(x, y, 'o', markersize=0.5)
plt.plot(circle_x, circle_y)

plt.xlabel("x")
plt.ylabel("y")

# if the sqrt(x^2+y^2)<1, then it must be within our unit circle, we can remove the inefficient sqrt function by squaring both sides of the inequality

incircle = x ** 2 + y ** 2 <= 1

pi = float(np.sum(incircle))/float(len(incircle))

print("pi: " + str(pi*4))

# visualise error



cumulative_ratios=( np.cumsum(incircle) / np.arange(1,times+1))

print(cumulative_ratios*4)

# now we plot this array of increasingly good approximations of pi, and visually compare it to the true value of pi

pis=cumulative_ratios*4

plt.figure()

approx_pis, = plt.plot(pis)
pi, = plt.plot(np.repeat(np.pi, times))

plt.ylim(3.1, 3.3)
plt.xlabel("Sample size")

plt.legend([approx_pis,pi],["Approximation", "Exact value"])

# plot the std against the sample size. calculated in the functions defined earlier in the code

plt.figure()
stdevs, = plt.plot(cumstd(pis))
plt.legend([stdevs], ["Standard deviation"])
plt.xlabel("Sample size")

plt.show()