import numpy as np
import pandas as pd

df = pd.read_csv('ErosData96Frames.csv')

result = pd.DataFrame(columns=['Frame', 'Curve'])

for i in range(df.shape[0]):
    frame = df['Frame'][i]
    curve = df['Curve'][i]

    nc = 10**(-0.4 * curve)
    result = result._append({'Frame': frame, 'Curve': nc}, ignore_index=True)

print(result)

result.to_csv('ErosDataNormalized.csv', index=False)
