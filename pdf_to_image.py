import subprocess
import os
import time

cwd = os.getcwd()
files = os.listdir()

for file in files:
    if '.pdf' in file.lower():
            # convert pdf to image
            cmd = ["magick", "-density", "150", os.path.join(cwd, file), "-quality", "90", os.path.join(cwd, '{}.tiff'.format(file))]
            subprocess.call(cmd, shell=True)

