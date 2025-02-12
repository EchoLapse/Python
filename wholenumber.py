import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'C:/Users/Ani Pulavarthi/Documents/Python/ErosDataFrames.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Initialize an empty DataFrame to store the results
result = pd.DataFrame(columns=['Frame', 'Curve'])

# Loop through whole numbers from 0 to 96
for i in range(96):
    # Calculate the distance of each frame value to the current whole number
    df['distance_to_whole'] = np.abs(df['Frame'] - i)
    
    # Find the row with the smallest distance to the current whole number
    closest_row = df.loc[df['distance_to_whole'].idxmin()]
    
    # Append the closest row to the result DataFrame
    result = result._append({'Frame': closest_row['Frame'], 'Curve': closest_row['Curve']}, ignore_index=True)

# Print the result
print(result)

# Optionally, save the result to a new CSV file
result.to_csv('closest_to_whole_0_to_95.csv', index=False)