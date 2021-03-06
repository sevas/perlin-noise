#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Mon May 31 21:42:43 2010"



import numpy as np
import matplotlib.pyplot as plt
import noise
import time


def main():
    w, h = 512,512
    n = 8

    noise_values = np.zeros((w, h))

    time_before = time.time()
    for i in range(w-1):
        for j in range(h-1):
            x, y = float(i)/(w-1), float(j)/(h-1)
            noise_values[i, j] = noise.make_turbulence_2D(x, y, n)

    print "Time elapsed : %f seconds [size=(%d, %d), fractal=%d]" % (time.time() - time_before, w, h, n)
    values = noise_values
    #normalize & show
    values/=values.max()
    plt.imshow(values)#, cmap=plt.cm.gray)
    plt.colorbar()
    #plt.show()
    plt.savefig("../turbulence_mpl.png")


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "profile":
        import cProfile
        command = """main()"""
        cProfile.runctx( command, globals(), locals(),
                         filename="demo_matplotlib_%s.profile" % sys.argv[2] )
    else:
        main()
