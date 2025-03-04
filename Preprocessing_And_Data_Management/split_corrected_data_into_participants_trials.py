import pandas as pd
import os


data = pd.read_csv('/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Corrected EMIP Dataset/finalset_line_part.csv')

output_dir = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials'

grouped = data.groupby(['participant', 'trial'])

for (participant, trial), group in grouped:
    participant_dir = os.path.join(output_dir, f"participant{participant}")
    os.makedirs(participant_dir, exist_ok=True)
    first_row = group.iloc[0]
    first_row_code_file = first_row['code_file']

    code_file = ''
    if first_row_code_file == "rectangle_java2.jpg" or first_row_code_file == "rectangle_java.jpg": 
       code_file = "rectangle_java"
    elif first_row_code_file == "vehicle_java2.jpg" or first_row_code_file == "vehicle_java.jpg": 
        code_file = "vehicle_java"
    elif first_row_code_file == "vehicle_python2.jpg" or first_row_code_file == "vehicle_python.jpg": 
        code_file = "vehicle_python"
    elif first_row_code_file == "rectangle_python2.jpg" or first_row_code_file == "rectangle_python.jpg": 
       code_file = "rectangle_python"
    else:
       raise ValueError(f"Unexpected code_file value: {first_row_code_file}")
    

    filename = f"participant{participant}_trial{trial}_{code_file}.csv"
    filepath = os.path.join(participant_dir, filename)
    group.to_csv(filepath, index=False)
    print(filepath)
    
    
### This program manages the corrected data in following structure: 
### One directory for each participant and all trials of that participant are stored in seperated csv files in this directory. 
