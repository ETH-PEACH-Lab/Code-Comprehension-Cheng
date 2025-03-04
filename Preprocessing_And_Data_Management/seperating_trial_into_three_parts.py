import os
import pandas as pd

input_dir = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials_Complexity'
output_dir = '/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials_Complexity_3Stages'

os.makedirs(output_dir, exist_ok=True)

for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)

    if os.path.isdir(participant_path):
        participant_output_path = os.path.join(output_dir, participant_folder)
        os.makedirs(participant_output_path, exist_ok=True)

        for trial_file in os.listdir(participant_path):
            trial_file_path = os.path.join(participant_path, trial_file)
            df = pd.read_csv(trial_file_path)

            length = len(df) // 3

            part1 = df.iloc[:length].copy()
            part1['stage'] = 'stage1'

            part2 = df.iloc[length:2*length].copy()
            part2['stage'] = 'stage2'

            part3 = df.iloc[2*length:].copy()
            part3['stage'] = 'stage3'

            base_filename = os.path.splitext(trial_file)[0]
            output_file_part1 = os.path.join(participant_output_path, f"{base_filename}_part1.csv")
            output_file_part2 = os.path.join(participant_output_path, f"{base_filename}_part2.csv")
            output_file_part3 = os.path.join(participant_output_path, f"{base_filename}_part3.csv")

            part1.to_csv(output_file_part1, index=False)
            part2.to_csv(output_file_part2, index=False)
            part3.to_csv(output_file_part3, index=False)

print("Seperating each trial into 3 stages. Results saved in Participant_Trials_Complexity_3Stages")

## Each trial is divided into three equally long time frames based on 3-stages hypothesis 
## A new column "stage" is appended to the original data
## The divided data are stored in seperated csv files