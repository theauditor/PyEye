PyEye
======
A python binding for tesseract.
This is a python binding for tesseract tested in linux. It makes use of the PIL library. 

Requirements
------------
You need to install tesseract ocr tool for this binding to work.
It also require the python PIL library.
  $ apt-get install tesseract-ocr

Use
---
Copy pyeye.py to the working directory
   from pyeye import *
   from PIL import Image
   Im = Image.open('example.png')
   print riptext(Im)






