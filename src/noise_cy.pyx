# encoding: utf-8
# cython: profile=True

from __future__ import division
import numpy as np
cimport numpy as np
cimport cython


cdef extern from "math.h":
    cdef double floor(double)
    cdef double cos(double)
    cdef double sin(double)
    cdef double fabs(double)



def get_gradient2D(int i, int j, np.ndarray[int] p, gradients2D):
    cdef int I, J
    I = i & 0xff
    J =	j & 0xff
    cdef int idx1 = (I + p[J])&0xff
    cdef int idx = p[idx1] % 8
    return gradients2D[idx]


cdef double lerp(double a, double b, double alpha):
    return a*(1.0-alpha) + b*(alpha)



cdef double dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]



cdef double f(double t):
    return (t * ( t * ( t * (6.0*t**2 - 15.0*t + 10.0))))




def noise2D(double x, double y, np.ndarray[int] p, gradients2D):
    cdef int i, j 
    i = int(floor(x))
    j =	int(floor(y))
    g00 = get_gradient2D(i,   j, p, gradients2D)
    g01 = get_gradient2D(i,   j+1, p, gradients2D)
    g10 = get_gradient2D(i+1, j, p, gradients2D)
    g11 = get_gradient2D(i+1, j+1, p, gradients2D)
 
    cdef double u, v 
    u = (x-i)
    v =	(y-j)
 
    # intepolation ramps
    cdef double n00 = dot(g00, (u, v))
    cdef double n01 = dot(g01, (u, v-1))
    cdef double n10 = dot(g10, (u-1, v))
    cdef double n11 = dot(g11, (u-1, v-1))
 
    # blending
    cdef double nx0 = lerp(n00, n10, f(u))
    cdef double nx1 = lerp(n01, n11, f(u))
 
    cdef double nxy = lerp(nx0, nx1, f(v))
 
    return nxy



def make_turbulence2D(double x, double y, int n_octaves, double lacunarity, double gain, np.ndarray[int] p, gradients2D):
    cdef double sum = 0.0
    cdef double freq = 1.0
    cdef ampl = 0.5
    cdef int i
    for i in range(n_octaves):
        sum += fabs(noise2D(x*freq, y*freq, p, gradients2D)) * ampl
        freq *= lacunarity  # 2.0**i
        ampl *= gain         # 0.5**
    return sum



def make_turbulence_texture(int w, int h, int n_octaves,  np.ndarray[int] p, gradients2D):
    cdef np.ndarray[double, ndim=2] out = np.zeros((w,h))
    cdef int i, j
    cdef double x, y
    for i in range(w-1):
        for j in range(h-1):
            x, y = i/(w - 1), j/(h - 1)
            val = make_turbulence2D(x, y, n_octaves, 2.0, 0.5, p, gradients2D)
            out[i, j] = val
    return out
