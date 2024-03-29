# -*- coding: utf-8 -*-
#PyEye 0.1 - Nocturnal Nickel
#Copyright (C) 2014 Blaise M Crowly  - All rights reserved
#Created at Xincoz [xincoz.com]
#GPL v3

"""This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.)"""

"""This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details."""

from PIL import Image
import os
import subprocess

def riptext(Img):
    Img.save(".tmptif.tif")
    Com = ["tesseract", ".tmptif.tif", ".ripdata"]
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(Com, stdout=FNULL, stderr=subprocess.STDOUT)
    Com = "cat .ripdata.txt"
    Output = subprocess.check_output(Com, shell=True)
    os.remove('.tmptif.tif')
    os.remove('.ripdata.txt')
    return Output
