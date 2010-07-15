from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [Extension("noise_cy", ["noise_cy.pyx"], libraries=["m"], include_dirs = [np.get_include()])]

setup(
  name = 'perlin_noise',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
