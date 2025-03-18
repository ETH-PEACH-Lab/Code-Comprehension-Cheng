import pandas as pd
import os

input_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials'
output_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Complexity_New_Categorization'

os.makedirs(output_dir, exist_ok=True)

complexity_map = {
    "rectangle_java.jpg": "A", "rectangle_java2.jpg": "A",
     "vehicle_java.jpg": "A", "vehicle_java2.jpg": "A",
    "rectangle_python.jpg": "B", "rectangle_python2.jpg": "B",
    "vehicle_python.jpg": "C", "vehicle_python2.jpg": "C"
}

for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)

    if os.path.isdir(participant_path):
        participant_output_path = os.path.join(output_dir, participant_folder)
        os.makedirs(participant_output_path, exist_ok=True)

        for trial_file in os.listdir(participant_path):
            trial_file_path = os.path.join(participant_path, trial_file)

            df = pd.read_csv(trial_file_path)

            code_file = df['code_file'].iloc[0]
            complexity = complexity_map.get(code_file, 'Unknown')

            df['complexity'] = complexity

            output_file_path = os.path.join(participant_output_path, trial_file)
            
            df.to_csv(output_file_path, index=False)

                
print("Added complexity groups. Results saved in Participant_Trials_Complexity_New_Categorization")

### This program adds an additional column "complexity" to the original data
### The complexity is categorized in 2 groups, A and B with group A more complex 
### The complexity of original code snippet is determined by both cyclomatic complexity and source code linearity 