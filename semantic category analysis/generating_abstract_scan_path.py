import os
import pandas as pd

input_dir = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Semantic_Category"
output_file = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Abstract_Scan_Path/abstract_scan_path_summary.csv"

all_rows = []

for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)
    if not os.path.isdir(participant_path):
        continue

    for trial_file in os.listdir(participant_path):
        trial_path = os.path.join(participant_path, trial_file)
        df = pd.read_csv(trial_path)

        trial = df["trial"].iloc[0]
        participant = df["participant"].iloc[0]
        code_file = df["code_file"].iloc[0]
        code_language = df["code_language"].iloc[0]
        result = df["Comprehension_Question_Result"].iloc[0]
        complexity = df["complexity"].iloc[0]
        expertise = df["expertise"].iloc[0]

        path = " → ".join(df["semantic_category"].astype(str).tolist())

        all_rows.append({
            "trial": trial,
            "participant": participant,
            "code_file": code_file,
            "code_language": code_language,
            "Comprehension_Question_Result": result,
            "complexity": complexity,
            "expertise": expertise,
            "scan_path": path
        })

result_df = pd.DataFrame(all_rows)

os.makedirs(os.path.dirname(output_file), exist_ok=True)

result_df.to_csv(output_file, index=False)