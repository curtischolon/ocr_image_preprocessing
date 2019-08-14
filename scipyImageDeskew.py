import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.ndimage import interpolation as inter
import os

def find_score(arr, angle):
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score

for file in os.listdir():
    if file.endswith('.tiff'):  # do something
        img = Image.open(file)
        file = file.replace('_.tiff', '_')

        # convert to binary
        wd, ht = img.size
        pix = np.array(img.convert('1').getdata(), np.uint8)
        bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)
        # plt.imshow(bin_img, cmap='gray')
        # plt.savefig(f'{file}_binary.jpeg')

        delta = 1
        limit = 5
        angles = np.arange(-limit, limit+delta, delta)
        scores = []
        for angle in angles:
            hist, score = find_score(bin_img, angle)
            scores.append(score)

        best_score = max(scores)
        best_angle = angles[scores.index(best_score)]

        # correct skew
        data = inter.rotate(img, best_angle, reshape=False, order=0)
        img = Image.fromarray((data).astype('uint8')).convert('RGB')
        img.save(f'{file}_corrected.tiff')
