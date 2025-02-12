from PIL import Image, ImageStat
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def getLuminosity(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


#figure out if the user wants to generate a CSV file or just a graph
access_type = input("1 for CSV gen & 2 for Graph only: ")
input_dir = input("file: ")

output_file = input_dir + '.csv'

if access_type == '1':
    
    #sets the working directory to the folder with the images
    os.chdir("C:/Users/Ani Pulavarthi/Documents/Final renders")
    os.chdir(input_dir)
    print(os.getcwd())

    # Initialize an empty DataFrame to store the results
    result = pd.DataFrame(columns=['Frame', 'Curve'])

    i = 0

    for im in os.listdir():
        lum = getLuminosity(im)
        print(lum)
        result = result._append({'Frame': i, 'Curve': lum}, ignore_index=True)
        i += 1

    print(result)

    os.chdir("C:/Users/Ani Pulavarthi/Documents/Light Curve CSV")

    result.to_csv(output_file, index=False)



os.chdir("C:/Users/Ani Pulavarthi/Documents/Light Curve CSV")
result = pd.read_csv(output_file)
print(result)

plt.figure(figsize=(12, 6))
plt.title('Luminosity Over Time')
plt.ylabel('Luminosity')
plt.xlabel('Frame')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, result.shape[0], 5), fontsize=14)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)  
plt.plot(result['Frame'], result['Curve'], marker='', linestyle='-', color='c', label='Luminosity', linewidth=2)

plt.show()

