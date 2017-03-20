#!/usr/bin/python

from distutils.core import setup, Extension

module_extend = Extension(¡®extend¡¯,[extend.c'])

setup ( name = 'Extend', version = '1.0', 
description="This is a Python extend Demo", 
ext_modules=[module_extend])
