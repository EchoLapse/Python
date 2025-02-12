import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('ErosDataNormalized.csv')

plt.figure(figsize=(12, 6))
plt.title('Luminosity Over Time')
plt.ylabel('Luminosity')
plt.xlabel('Frame')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, df.shape[0], 5), fontsize=14)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)

plt.plot(df['Frame'], df['Curve'], marker='', linestyle='-', color='c', label='Magnitude', linewidth=2)
#plt.gca().invert_yaxis()
plt.show()