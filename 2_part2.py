#!/usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

myx = []

with open("new.txt","r") as reader:
    for line in reader.readlines():
        myx.append(float(line))

# create histogram of our data
n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

# show figure (program only ends once closed
plt.show()
