import pandas as pd
import os

dir_path = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials'

### In some trials, the same data is replicated by twice.
### It's unclear why it is so, but we simply deleted dupliated ones. 

for root, _, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.csv'):
            filepath = os.path.join(root, file)

            data = pd.read_csv(filepath)

            columns_to_exclude = ['Unnamed: 0']
            columns_to_check = [col for col in data.columns if col not in columns_to_exclude]

            before_rows = len(data)
            deduplicated_data = data.drop_duplicates(subset=columns_to_check)
            after_rows = len(deduplicated_data)

            if before_rows != after_rows:
                deduplicated_data.to_csv(filepath, index=False)
                print(f"File {filepath}: Removed {before_rows - after_rows} duplicated rows.")

# In file participant196_trial2_rectangle_java.csv, we notice that there are two versions for the same trial
# One version with quality = 90 and another version with quality = 85
# Therefore, we simply delete the version with quality = 85

file_path = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials/participant196/participant196_trial2_vehicle_java.csv'

# Load the CSV file
data = pd.read_csv(file_path)

filtered_data = data[data['quality'] != 85]

filtered_data.to_csv(file_path, index=False)

print(f"Rows with quality = 85 have been removed from {file_path}.")



                