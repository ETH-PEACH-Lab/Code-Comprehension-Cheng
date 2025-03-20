import pandas as pd
import os

input_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials'
output_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Comprehension_Results'
metadata_file = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/emip_dataset/emip_metadata.csv'

os.makedirs(output_dir, exist_ok=True)

complexity_map = {
    "rectangle_java.jpg": "A", "rectangle_java2.jpg": "A",
    "rectangle_python.jpg": "A", "rectangle_python2.jpg": "A",
    "vehicle_java.jpg": "B", "vehicle_java2.jpg": "B",
    "vehicle_python.jpg": "B", "vehicle_python2.jpg": "B"
}

metadata = pd.read_csv(metadata_file)

def get_comprehension_result(participant_id, code_file):

    participant_data = metadata[metadata['id'] == participant_id]
    
    if participant_data.empty:
        raise ValueError(f"Error: Participant {participant_id} not found in metadata.")
    
    if "rectangle" in code_file:
        correctness = participant_data['correct_rectangle'].values[0]
    elif "vehicle" in code_file:
        correctness = participant_data['correct_vehicle'].values[0]
    else:
        raise ValueError(f"Error: Participant {participant_id} not found in metadata.")
    
    return correctness


for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)

    if os.path.isdir(participant_path):
        participant_output_path = os.path.join(output_dir, participant_folder)
        os.makedirs(participant_output_path, exist_ok=True)

        for trial_file in os.listdir(participant_path):
            trial_file_path = os.path.join(participant_path, trial_file)

            df = pd.read_csv(trial_file_path)

            participant_id = df['participant'].iloc[0]

            code_file = df['code_file'].iloc[0]

            comprehension_result = get_comprehension_result(participant_id, code_file)

            df['Comprehension_Question_Result'] = comprehension_result

            complexity = complexity_map.get(code_file, 'Unknown')

            df['complexity'] = complexity

            output_file_path = os.path.join(participant_output_path, trial_file)
            df.to_csv(output_file_path, index=False)

print("Results saved in Participant_Trials_Comprehension")

### This program extracts the correctness of participant's answer to the question of the comprehension question
### and appends a new column "Comprehension_Question_Result" as well as the complexity level "complexity" (old categorization approach)