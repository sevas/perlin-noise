#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Mon May 31 21:42:43 2010"



import numpy as np
import matplotlib.pyplot as plt
import noise


if __name__ == '__main__':
    w, h = 256,256
    n = 8
    fractal_sum = np.zeros((w, h))
    turbulence = np.zeros_like(fractal_sum)
    ridges = np.zeros_like(fractal_sum)
    noise_values = np.zeros_like(fractal_sum)

    for i in range(w-1):
        for j in range(h-1):
            x, y = float(i)/(w), float(j)/(h)
            #fractal_sum[i, j] = noise.make_fractal_sum_2D(x, y, n)
            #turbulence[i, j] = noise.make_turbulence_2D(x, y, n)
            #noise_values[i, j] = noise.make_ridgedmf(x, y, n, 5.0)
            noise_values[i, j] = noise.make_marble_2D(x, y, n)
        
    values = noise_values
    #normalize & show 
    values/=values.max()
    plt.imshow(values, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

