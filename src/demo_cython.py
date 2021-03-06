#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import noise_cy as noise
import math as m
import time



_p = [51, 3, 190, 211, 218, 30, 27, 64, 65, 158, 42, 99, 78, 48,
 238, 245, 228, 243, 38, 98, 2, 115, 226, 210, 36, 87, 9, 101, 23, 63,
 40, 154, 34, 181, 20, 168, 104, 167, 144, 165, 28, 68, 19, 247, 14,
 171, 44, 80, 102, 222, 159, 135, 49, 84, 17, 95, 209, 117, 136, 235,
 237, 197, 206, 143, 217, 59, 246, 239, 5, 160, 43, 103, 176, 35, 45,
 72, 113, 26, 193, 172, 227, 57, 131, 153, 70, 123, 139, 156, 255, 75,
 12, 204, 97, 61, 1, 105, 91, 121, 108, 180, 134, 189, 169, 50, 185,
 71, 194, 253, 79, 252, 41, 215, 219, 93, 145, 127, 232, 90, 7, 73,
 83, 230, 201, 170, 60, 138, 100, 150, 220, 21, 147, 141, 16, 25, 110,
 195, 216, 24, 109, 250, 89, 88, 236, 233, 116, 202, 112, 130, 85, 52,
 107, 6, 163, 129, 125, 119, 157, 221, 186, 140, 114, 122, 207, 229,
 22, 18, 198, 39, 56, 86, 111, 46, 62, 8, 191, 224, 69, 249, 15, 67,
 132, 234, 173, 182, 124, 240, 251, 58, 244, 241, 96, 148, 199, 74,
 212, 94, 133, 126, 178, 254, 242, 231, 174, 76, 0, 55, 183, 29, 146,
 77, 208, 188, 213, 164, 161, 53, 200, 33, 203, 162, 11, 166, 179,
 187, 196, 248, 151, 92, 177, 32, 81, 82, 31, 155, 120, 10, 4, 223,
 184, 175, 37, 205, 225, 66, 128, 214, 13, 142, 118, 54, 137, 152,
 192, 47, 106, 149]

#p = range(256)
#random.shuffle(p)

p = np.array(_p)
TAU = 2 * m.pi
N = 8

gradients = np.ndarray((N, 2))
gradients[:,0] = [m.cos(i * TAU / N) for i in range(N)]
gradients[:,1] = [m.sin(i * TAU / N) for i in range(N)]


def main():
    w, h = 512,512
    n = 8

    time_before = time.time()
    texture =  noise.make_turbulence_texture(w,h, n, p, gradients)
    print "Time elapsed : %f seconds [size=(%d, %d), fractal=%d]" % (time.time() - time_before, w, h, n)


    #normalize & show
    texture/=texture.max()
    plt.imshow(texture)#, cmap=plt.cm.gray)
    plt.colorbar()
    plt.savefig("../turbulence_cy.png")
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "profile":
        import pstats, cProfile
        import pyximport
        pyximport.install()
        command = """main()"""
        cProfile.runctx( command, globals(), locals(),
                         filename="demo_cython_%s.profile" % sys.argv[2])
    else:
        main()



