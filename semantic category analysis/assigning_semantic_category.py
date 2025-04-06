import pandas as pd
import os

input_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Comprehension_Results'
output_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Semantic_Category'

os.makedirs(output_dir, exist_ok=True)

semantic_category_mapping_rectangle_java = [
    {"category": "Class Declaration", "line_range": (1, 1), "part_range": (1, 3)},
    {"category": "Variable Declaration", "line_range": (2, 2), "part_range": (1, 9)},
    {"category": "Constructor Declaration", "line_range": (3, 3), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (3, 3), "part_range": (4, 14)},
    {"category": "Assignment", "line_range": (4, 4), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (5, 5), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (6, 6), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (7, 7), "part_range": (1, 3)},
    {"category": "Method Declaration", "line_range": (9, 9), "part_range": (1, 3)},
    {"category": "Parameter", "line_range": (9, 9), "part_range": (4, 5)},
    {"category": "Return", "line_range": (9, 9), "part_range": (7, 7)},
    {"category": "Variable", "line_range": (9, 9), "part_range": (8, 8)},
    {"category": "Operator", "line_range": (9, 9), "part_range": (9, 9)},
    {"category": "Variable", "line_range": (9, 9), "part_range": (10, 10)},
    {"category": "Method Declaration", "line_range": (10, 10), "part_range": (1, 3)},
    {"category": "Parameter", "line_range": (10, 10), "part_range": (4, 5)},
    {"category": "Return", "line_range": (10, 10), "part_range": (7, 7)},
    {"category": "Variable", "line_range": (10, 10), "part_range": (8, 8)},
    {"category": "Operator", "line_range": (10, 10), "part_range": (9, 9)},
    {"category": "Variable", "line_range": (10, 10), "part_range": (10, 10)},
    {"category": "Method Declaration", "line_range": (11, 11), "part_range": (1, 3)},
    {"category": "Parameter", "line_range": (11, 11), "part_range": (4, 5)},
    {"category": "Return", "line_range": (11, 11), "part_range": (7, 7)},
    {"category": "Method Call", "line_range": (11, 11), "part_range": (8, 10)},
    {"category": "Operator", "line_range": (11, 11), "part_range": (11, 11)},
    {"category": "Method Call", "line_range": (11, 11), "part_range": (12, 14)},
    {"category": "Method Declaration", "line_range": (12, 12), "part_range": (1, 4)},
    {"category": "Parameter", "line_range": (12, 12), "part_range": (6, 9)},
    {"category": "Variable Declaration", "line_range": (13, 13), "part_range": (1, 2)},
    {"category": "Operator", "line_range": (13, 13), "part_range": (3, 3)},
    {"category": "Object Instantiation", "line_range": (13, 13), "part_range": (4, 5)},
    {"category": "Argument", "line_range": (13, 13), "part_range": (7, 13)},
    {"category": "Method Call", "line_range": (14, 14), "part_range": (1, 1)},
    {"category": "Argument", "line_range": (14, 14), "part_range": (3, 3)},
    {"category": "Variable Declaration", "line_range": (15, 15), "part_range": (1, 2)},
    {"category": "Operator", "line_range": (15, 15), "part_range": (3, 3)},
    {"category": "Object Instantiation", "line_range": (15, 15), "part_range": (4, 5)},
    {"category": "Argument", "line_range": (15, 15), "part_range": (7, 13)},
    {"category": "Method Call", "line_range": (16, 16), "part_range": (1, 1)},
    {"category": "Argument", "line_range": (16, 16), "part_range": (3, 3)},
    {"category": "Punctuation", "line_range": (1, 20), "part_range": (1, 30)}  
]



semantic_category_mapping_vehicle_java = [
    {"category": "Class Declaration", "line_range": (1, 1), "part_range": (1, 3)},
    {"category": "Variable Declaration", "line_range": (2, 2), "part_range": (1, 4)},
    {"category": "Variable Declaration", "line_range": (3, 3), "part_range": (1, 4)},
    {"category": "Constructor Declaration", "line_range": (4, 4), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (4, 4), "part_range": (4, 11)},
    {"category": "Assignment", "line_range": (5, 5), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (6, 6), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (7, 7), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (8, 8), "part_range": (1, 3)},
    {"category": "Method Declaration", "line_range": (10, 10), "part_range": (1, 3)},
    {"category": "Parameter", "line_range": (10, 10), "part_range": (5, 6)},
    {"category": "Conditional Statement", "line_range": (11, 11), "part_range": (1, 10)},
    {"category": "Assignment", "line_range": (12, 12), "part_range": (1, 3)},
    {"category": "Conditional Statement", "line_range": (13, 13), "part_range": (2, 2)},
    {"category": "Assignment", "line_range": (14, 14), "part_range": (1, 5)},
    {"category": "Return", "line_range": (16, 16), "part_range": (1, 2)},
    {"category": "Method Declaration", "line_range": (18, 18), "part_range": (1, 4)},
    {"category": "Parameter", "line_range": (18, 18), "part_range": (6, 9)},
    {"category": "Variable Declaration", "line_range": (19, 19), "part_range": (1, 2)},
    {"category": "Operator", "line_range": (19, 19), "part_range": (3, 3)},
    {"category": "Object Instantiation", "line_range": (19, 19), "part_range": (4, 5)},
    {"category": "Argument", "line_range": (19, 19), "part_range": (7, 11)},
    {"category": "Method Call", "line_range": (20, 20), "part_range": (1, 1)},
    {"category": "Argument", "line_range": (20, 20), "part_range": (3, 3)},
    {"category": "Punctuation", "line_range": (1, 22), "part_range": (1, 30)}  
]


semantic_category_mapping_rectangle_python = [
    {"category": "Class Declaration", "line_range": (1, 1), "part_range": (1, 2)},
    {"category": "Method Declaration", "line_range": (2, 2), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (2, 2), "part_range": (3, 11)},
    {"category": "Assignment", "line_range": (3, 3), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (4, 4), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (5, 5), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (6, 6), "part_range": (1, 3)},
    {"category": "Method Declaration", "line_range": (7, 7), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (7, 7), "part_range": (4, 4)},
    {"category": "Return", "line_range": (7, 7), "part_range": (7, 7)},
    {"category": "Variable", "line_range": (7, 7), "part_range": (8, 8)},
    {"category": "Operator", "line_range": (7, 7), "part_range": (9, 9)},
    {"category": "Variable", "line_range": (7, 7), "part_range": (10, 10)},
     {"category": "Method Declaration", "line_range": (8, 8), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (8, 8), "part_range": (4, 4)},
    {"category": "Return", "line_range": (8, 8), "part_range": (7, 7)},
    {"category": "Variable", "line_range": (8, 8), "part_range": (8, 8)},
    {"category": "Operator", "line_range": (8, 8), "part_range": (9, 9)},
    {"category": "Variable", "line_range": (8, 8), "part_range": (10, 10)},
    {"category": "Method Declaration", "line_range": (9, 9), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (9, 9), "part_range": (4, 4)},
    {"category": "Return", "line_range": (9, 9), "part_range": (7, 7)},
    {"category": "Method Call", "line_range": (9, 9), "part_range": (8, 10)},
    {"category": "Operator", "line_range": (9, 9), "part_range": (11, 11)},
    {"category": "Method Call", "line_range": (9, 9), "part_range": (12, 14)},
    {"category": "Variable Declaration", "line_range": (10, 10), "part_range": (1, 1)},
    {"category": "Operator", "line_range": (10, 10), "part_range": (2, 2)},
    {"category": "Object Instantiation", "line_range": (10, 10), "part_range": (3, 3)},
    {"category": "Argument", "line_range": (10, 10), "part_range": (5, 11)},
    {"category": "Method Call", "line_range": (11, 11), "part_range": (1, 1)},
    {"category": "Method Call", "line_range": (11, 11), "part_range": (2, 2)},
    {"category": "Variable Declaration", "line_range": (12, 12), "part_range": (1, 1)},
    {"category": "Operator", "line_range": (12, 12), "part_range": (2, 2)},
    {"category": "Object Instantiation", "line_range": (12, 12), "part_range": (3, 3)},
    {"category": "Argument", "line_range": (12, 12), "part_range": (5, 11)},
    {"category": "Method Call", "line_range": (13, 13), "part_range": (1, 1)},
    {"category": "Method Call", "line_range": (13, 13), "part_range": (2, 2)},
    {"category": "Punctuation", "line_range": (1, 14), "part_range": (1, 30)}  
]


semantic_category_mapping_vehicle_python = [
    {"category": "Class Declaration", "line_range": (1, 1), "part_range": (1, 2)},
    {"category": "Method Declaration", "line_range": (2, 2), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (2, 2), "part_range": (4, 10)},
    {"category": "Assignment", "line_range": (3, 3), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (4, 4), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (5, 5), "part_range": (1, 3)},
    {"category": "Assignment", "line_range": (6, 6), "part_range": (1, 3)},
    {"category": "Method Declaration", "line_range": (7, 7), "part_range": (1, 2)},
    {"category": "Parameter", "line_range": (7, 7), "part_range": (4, 6)},
    {"category": "Conditional Statement", "line_range": (8, 8), "part_range": (1, 8)},
    {"category": "Assignment", "line_range": (9, 9), "part_range": (1, 3)},
    {"category": "Conditional Statement", "line_range": (10, 10), "part_range": (1, 1)},
    {"category": "Assignment", "line_range": (11, 11), "part_range": (1, 5)},
    {"category": "Return", "line_range": (12, 12), "part_range": (1, 2)},
    {"category": "Variable Declaration", "line_range": (13, 13), "part_range": (1, 1)},
    {"category": "Operator", "line_range": (13, 13), "part_range": (2, 2)},
    {"category": "Object Instantiation", "line_range": (13, 13), "part_range": (3, 3)},
    {"category": "Argument", "line_range": (13, 13), "part_range": (5, 9)},
    {"category": "Method Call", "line_range": (14, 14), "part_range": (1, 1)},
    {"category": "Argument", "line_range": (14, 14), "part_range": (3, 3)},
    {"category": "Punctuation", "line_range": (1, 15), "part_range": (1, 30)}  
]



def get_mapping_for_code_snippet(code_file):
    if code_file in ["rectangle_java.jpg", "rectangle_java2.jpg"]:
        return semantic_category_mapping_rectangle_java
    elif code_file in ["vehicle_java.jpg", "vehicle_java2.jpg"]:
        return semantic_category_mapping_vehicle_java
    elif code_file in ["rectangle_python.jpg", "rectangle_python2.jpg"]:
        return semantic_category_mapping_rectangle_python
    elif code_file in ["vehicle_python.jpg", "vehicle_python2.jpg"]:
        return semantic_category_mapping_vehicle_python
    else:
         raise ValueError(f"Unknown code_file: {code_file}")




def assign_semantic_category_for_row(row, mapping):
    line = row["line"]
    part = row["part"]
    for rule in mapping:
        if rule["line_range"][0] <= line <= rule["line_range"][1] and rule["part_range"][0] <= part <= rule["part_range"][1]:
            return rule["category"]
    raise ValueError(f"No semantic category found for token at line {line}, part {part}")
    


for participant_folder in os.listdir(input_dir):
    participant_path = os.path.join(input_dir, participant_folder)

    if os.path.isdir(participant_path):
        participant_output_path = os.path.join(output_dir, participant_folder)
        os.makedirs(participant_output_path, exist_ok=True)

        for trial_file in os.listdir(participant_path):
            trial_file_path = os.path.join(participant_path, trial_file)

            df = pd.read_csv(trial_file_path)

            code_file = df['code_file'].iloc[0]

            mapping = get_mapping_for_code_snippet(code_file)

            df["semantic_category"] = df.apply(lambda row: assign_semantic_category_for_row(row, mapping), axis=1)

            output_file_path = os.path.join(participant_output_path, trial_file)
            df.to_csv(output_file_path, index=False)

print("Results saved in Participant_Trials_Semantic_Category")
