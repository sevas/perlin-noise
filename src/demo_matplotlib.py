#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Mon May 31 21:42:43 2010"



import numpy as np
import matplotlib.pyplot as plt
import noise


if __name__ == '__main__':
    w, h = 256,256
    p, n = 1.0, 5
    values = np.zeros((w, h))
    for i in range(w-1):
        for j in range(h-1):
            x, y = float(i)/(w), float(j)/(h)
            values[i, j] = noise.perlin_noise(x, y, p, n) 


    #normalize & show 
    values/=values.max()
    plt.imshow(values, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

