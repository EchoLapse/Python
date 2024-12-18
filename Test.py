from PIL import Image, ImageStat
import os
import matplotlib.pyplot as plt
import numpy as np

def getLuminosity(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]

os.chdir('..')
os.chdir('Final renders')
os.chdir('Test #6')

luminosities = []

# Filter out non-image files
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

for im in os.listdir():
    if im.lower().endswith(image_extensions):
        print(getLuminosity(im))
        luminosities.append(getLuminosity(im))

plt.figure(figsize=(12, 6))
plt.title('Luminosity Over Time')
plt.ylabel('Luminosity')
plt.xlabel('Frame')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)  

x_values = np.arange(len(luminosities))
plt.xticks(np.arange(0, len(luminosities), 5), fontsize=14)
plt.plot(x_values, luminosities, marker='', linestyle='-', color='c', label='Luminosity', linewidth=2)

plt.show()