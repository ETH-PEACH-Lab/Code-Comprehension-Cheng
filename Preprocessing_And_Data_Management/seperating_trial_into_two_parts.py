import os
import pandas as pd

input_dir = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials_Complexity'
output_dir = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials_Complexity_2Stages'

os.makedirs(output_dir, exist_ok=True)

for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)

    if os.path.isdir(participant_path):
        participant_output_path = os.path.join(output_dir, participant_folder)
        os.makedirs(participant_output_path, exist_ok=True)

        for trial_file in os.listdir(participant_path):
            trial_file_path = os.path.join(participant_path, trial_file)
            
            df = pd.read_csv(trial_file_path)

            mid = len(df) // 2

            part1 = df.iloc[:mid].copy()
            part2 = df.iloc[mid:].copy()

            part1['stage'] = 'stage1'
            part2['stage'] = 'stage2'

            base_filename = trial_file.replace('.csv', '')
            part1_filename = f"{base_filename}_part1.csv"
            part2_filename = f"{base_filename}_part2.csv"

            part1_output_path = os.path.join(participant_output_path, part1_filename)
            part2_output_path = os.path.join(participant_output_path, part2_filename)

            part1.to_csv(part1_output_path, index=False)
            part2.to_csv(part2_output_path, index=False)

print("Separating each trial into 2 stages. Results saved in Participant_Trials_Complexity_2Stages")


## Each trial is divided into two equally long time frames based on 2-stages hypothesis 
## A new column "stage" is appended to the original data
## The divided data are stored in seperated csv files