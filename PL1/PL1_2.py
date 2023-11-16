# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:16:18 2023

@author: muldooaa
"""

import numpy as np
import matplotlib.pyplot as plt


#calculate the mean of the data
def cummean(arr):
 return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=float)

#use the mean to calculate the std
def cumstd(arr):
 return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2)

times=10000

area=2*4

x=np.random.rand(times)*2
y=np.random.rand(times)*4

curve_x=np.linspace(0, 5, 100)
curve_y=curve_x**2

fig2 = plt.figure()

fig2.set_size_inches(5, 5)

plt.ylim(0, 4)
plt.xlim(0, 2)

plt.xlabel("x")
plt.ylabel("y")

undergraph = y < x ** 2

plt.plot(x, y, 'o', markersize=0.5)
plt.plot(curve_x, curve_y)

plt.plot()

# get the chance of random point being below the graph

chanceinside = np.cumsum(undergraph)/np.arange(1, times+1)

farea=chanceinside*area

print(farea)
print(cumstd(farea))


plt.figure()

approxarea, = plt.plot(farea)
area, = plt.plot(np.repeat(8/3, times))

plt.xlabel("Sample size")

plt.legend([approxarea,area],["Approximation", "Exact value"])


# std graph

plt.figure()
stdevs, = plt.plot(cumstd(farea))
plt.legend([stdevs], ["Standard deviation"])
plt.xlabel("Sample size")