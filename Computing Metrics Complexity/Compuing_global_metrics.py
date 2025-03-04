import os
import pandas as pd
import NW_Algorithm as nw

# Story Order and Execution Order of each code snippet manually calculated

STORY_ORDER = {
    "rectangle_java.jpg": list(range(1, 19)),
    "rectangle_java2.jpg": list(range(1, 19)),
    "vehicle_java.jpg": list(range(1, 23)),
    "vehicle_java2.jpg": list(range(1, 23)),
    "rectangle_python.jpg": list(range(1, 14)),
    "vehicle_python.jpg": list(range(1, 15))
}

EXECUTION_ORDER = {
    "rectangle_java.jpg": [1, 2, 12, 13, 3, 4, 5, 6, 7, 8, 14, 11, 9, 10, 11, 15, 3, 4, 5, 6, 7, 8, 16, 11, 9, 10, 11, 17, 18],
    "rectangle_java2.jpg": [1, 2, 12, 13, 3, 4, 5, 6, 7, 8, 14, 11, 9, 10, 11, 15, 3, 4, 5, 6, 7, 8, 16, 11, 9, 10, 11, 17, 18],
    "vehicle_java.jpg": [1, 2, 3, 18, 19, 4, 5, 6, 7, 8, 9, 20, 10, 11, 13, 14, 15, 16, 17, 21, 22],
    "vehicle_java2.jpg": [1, 2, 3, 18, 19, 4, 5, 6, 7, 8, 9, 20, 10, 11, 13, 14, 15, 16, 17, 21, 22],
    "rectangle_python.jpg": [1, 10, 2, 3, 4, 5, 6, 11, 9, 7, 8, 12, 2, 3, 4, 5, 6, 13, 9, 7, 8],
    "vehicle_python.jpg": [1, 13, 2, 3, 4, 5, 6, 14, 7, 8, 10, 11, 12]
}

PARTICIPANT_TRIALS_DIR = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/Participant_Trials_Complexity"

EMIP_METADATA_FILE = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/emip_dataset/emip_metadata.csv"

OUTPUT_FILE = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/global_metrics_complexity_summary.csv"

metadata = pd.read_csv(EMIP_METADATA_FILE)

def get_gaze_path(data):
    gaze_path = []
    prev_line = None
    for line in data["line"]:
        if line != prev_line:
            gaze_path.append(line)
        prev_line = line
    return gaze_path

results = []

for root, _, files in os.walk(PARTICIPANT_TRIALS_DIR):
    for file in files:
        if file.endswith(".csv"):
            filepath = os.path.join(root, file)

            data = pd.read_csv(filepath)

            participant = int(file.split("_")[0].replace("participant", ""))
            trial = int(file.split("_")[1].replace("trial", ""))
            code_file = data.iloc[0]["code_file"]
            Complexity = data.iloc[0]['complexity']

            if "python" in code_file:
                programming_language = "Python"
            elif "java" in code_file:
                programming_language = "Java"
            else:
                programming_language = "Unknown"

            expertise = metadata.loc[metadata["id"] == participant, "expertise_programming"].values
            expertise_programming = expertise[0] 

            story_order = STORY_ORDER.get(code_file, [])
            execution_order = EXECUTION_ORDER.get(code_file, [])

            gaze_path = get_gaze_path(data)

            story_naive_score = nw.nwalign_and_compute_nw_score_naive(story_order, gaze_path)
            story_dynamic_repetitions, story_dynamic_score = nw.nwalign_and_compute_nw_score_dynamic(story_order, gaze_path)

            execution_naive_score = nw.nwalign_and_compute_nw_score_naive(execution_order, gaze_path)
            execution_dynamic_repetitions, execution_dynamic_score = nw.nwalign_and_compute_nw_score_dynamic(execution_order, gaze_path)

            
            results.append({
                "Participant": participant,
                "Trial": trial,
                "code_file": code_file,
                "Programming_Language": programming_language,
                "Expertise": expertise_programming,
                'Complexity': Complexity,
                "Story_Order_Naive_Score": story_naive_score,
                "Story_Order_Dynamic_Score": story_dynamic_score,
                "Story_Order_Dynamic_Repetitions": story_dynamic_repetitions,
                "Execution_Order_Naive_Score": execution_naive_score,
                "Execution_Order_Dynamic_Score": execution_dynamic_score,
                "Execution_Order_Dynamic_Repetitions": execution_dynamic_repetitions
            })

results_df = pd.DataFrame(results)
results_df.to_csv(OUTPUT_FILE, index=False)
print(f"Results saved to {OUTPUT_FILE}")

## No difference comparing to original version, except for appending the new column "complexity"