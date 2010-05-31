#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Sun May 30 20:36:45 2010"



import random
import math as m


#p = range(256)
#random.shuffle(p)

p = [51, 3, 190, 211, 218, 30, 27, 64, 65, 158, 42, 99, 78, 48,
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

        

gradients2D = []
for i in [0, m.pi/2, m.pi, 3*m.pi/2, m.pi/4, 3*m.pi/4, 5*m.pi/4, 7*m.pi/4]:
    gradients2D.append((m.cos(i), m.sin(i)))



def get_gradient2D(i, j):
    I, J = i & 0xff , j & 0xff
  
    idx = p[(I + p[J])&0xff] % len(gradients2D)
    return gradients2D[idx]



def lerp(a, b, alpha):
    return a*(1-alpha) + b*(alpha)

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]


def f(t):
    #return 3*t**2 - 2*t**3
    #return 6*t**5 - 15*t**4 + 10*t**3
    return (t * ( t * ( t * (6*t**2 - 15*t + 10))))


def noise(x, y):
    i, j = int(m.floor(x)), int(m.floor(y))
    g00 = get_gradient2D(i,   j)
    g01 = get_gradient2D(i,   j+1)
    g10 = get_gradient2D(i+1, j)
    g11 = get_gradient2D(i+1, j+1)

    u, v = (x-i), (y-j)

    # intepolation ramps
    n00 = dot(g00, (u, v))
    n01 = dot(g01, (u, v-1))
    n10 = dot(g10, (u-1, v))
    n11 = dot(g11, (u-1, v-1))

    # blending
    nx0 = lerp(n00, n10, f(u))
    nx1 = lerp(n01, n11, f(u))

    nxy = lerp(nx0, nx1, f(v))

    return nxy


def perlin_noise(x, y,  p, n):
    total = 0.0
    for i in range(n):
        freq = 2**i
        ampl = p**i

        total += noise(x * freq, y * freq) * ampl

    return total


def make_2D_array(w, h):
    array = []
    for i in range(h):
        array.append([0]*w)
    return array


def make_perlin_noise(w, h, p, n):
    noise_values = make_2D_array(w, h) 
    for i in range(w-1):
        for j in range(h-1):
            noise_values[i][j] = perlin_noise(float(i) / (w-1), float(j) / (h-1), p, n)
            
    return noise_values








