#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Mon May 31 21:42:43 2010"



import numpy as np
import matplotlib.pyplot as plt
import noise


if __name__ == '__main__':
    w, h = 512,512
    n = 5
    texture = np.zeros((w, h))

    for i in range(w-1):
        for j in range(h-1):
            x, y = float(i)/(w), float(j)/(h)
            #texture[i, j] = noise.make_fractal_sum_2D(x, y, n)
            #texture[i, j] = noise.make_turbulence_2D(x, y, n)
            texture[i, j] = noise.make_ridgedmf(x, y, n, 5.0)
            #texture[i, j] = noise.make_marble_2D(x, y, n)
       
    #normalize & show 
    texture /= texture.max()
    plt.imshow(texture)#, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

