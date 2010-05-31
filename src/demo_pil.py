#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Frederic De Groef (f.degroef@gmail.com)"
__date__   = "Mon May 31 21:41:05 2010"


from PIL import Image
import noise
import os



def make_image2D(values, num_octaves, persistence, outdir):
    w, h = len(values[0]), len(values)
    
    img = Image.new("L", (w, h), 0)
    for i in range(w):
        for j in range(h):
            img.putpixel((i, j), int(values[i][j]*256))

    outfile = outdir+"p_%.4f_n_%d.png" % (persistence, num_octaves)
    print "saving in %s" % outfile
    img.save(outfile)



def make_batch():
    PREFIX="./"
    outdir = PREFIX+"gradient_perlin_out/"
     
    try:
        os.mkdir(outdir)
    except:
        pass

    w, h = 128, 128

    for p in [0.1, 0.25, 0.5, 0.75, 1.0]:
        for n in range(1, 10):
            values = noise.make_perlin_noise(w, h, p, n)
            #values /= values.max()
            make_image2D(values, n, p, outdir)



def make_one():
    PREFIX="./"
    outdir = PREFIX+"gradient_perlin_out/"

    try:
        os.mkdir(outdir)
    except:
        pass

    w, h = 256, 256
    p = 0.5
    n = 4
    values = noise.make_perlin_noise(w, h, p, n)
    make_image2D(values, n, p, outdir)

if __name__ == '__main__':
    #make_one()
    make_batch()
