import pandas as pd
import os

dir_path = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials'

for root, _, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.csv'):
            filepath = os.path.join(root, file)
            data = pd.read_csv(filepath)

            if not data['timestamp'].is_monotonic_increasing:

                data = data.sort_values(by='timestamp')

                data.to_csv(filepath, index=False)
                print(f"File {filepath} was reordered by timestamp.")

## This program checks whether fixations in each trial is corrected sorted by timestamp. 