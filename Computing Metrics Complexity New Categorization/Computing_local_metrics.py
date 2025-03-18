import os
import pandas as pd
import numpy as np

participant_trials_dir = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Complexity_New_Categorization'
emip_metadata_file = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/emip_dataset/emip_metadata.csv'
output_file = '/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/local_metrics_complexity_new_categorization_summary.csv'

metadata = pd.read_csv(emip_metadata_file)

def compute_metrics(data, total_tokens):
    metrics = {
        'Vertical_Next_Text': 0,
        'Vertical_Later_Text': 0,
        'Horizontal_Later_Text': 0,
        'Regression_Rate': 0,
        'Line_Regression_Rate': 0,
        'Saccade_Length': 0,
        'Element_Coverage': 0
    }

    total_fixations = len(data)
    total_distance = 0

    for i in range(len(data) - 1):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]

        if current_row['line'] == next_row['line'] or current_row['line'] == next_row['line'] - 1:
            metrics['Vertical_Next_Text'] += 1


        if current_row['line'] <= next_row['line']:
            metrics['Vertical_Later_Text'] += 1

        if current_row['line'] == next_row['line'] and current_row['part'] <= next_row['part']:
            metrics['Horizontal_Later_Text'] += 1

        if current_row['line'] > next_row['line'] or (current_row['line'] == next_row['line'] and current_row['part'] > next_row['part']):
            metrics['Regression_Rate'] += 1

        if current_row['line'] == next_row['line'] and current_row['part'] > next_row['part']:
            metrics['Line_Regression_Rate'] += 1

        total_distance += np.sqrt((next_row['x_cord'] - current_row['x_cord'])**2 + (next_row['y_cord'] - current_row['y_cord'])**2)

    for key in ['Vertical_Next_Text', 'Vertical_Later_Text', 'Horizontal_Later_Text', 'Regression_Rate', 'Line_Regression_Rate']:
        metrics[key] = metrics[key] / total_fixations

    metrics['Saccade_Length'] = total_distance / (total_fixations - 1)

    metrics['Element_Coverage'] = len(data['token'].unique()) / total_tokens

    return metrics

results = []

for root, _, files in os.walk(participant_trials_dir):
    for file in files:
        if file.endswith('.csv'):

            filepath = os.path.join(root, file)

            participant = int(file.split('_')[0].replace('participant', ''))
            trial = int(file.split('_')[1].replace('trial', ''))

            data = pd.read_csv(filepath)
            total_tokens = 1

            Complexity = data.iloc[0]['complexity']


            code_file = data.iloc[0]['code_file']
            if 'python' in code_file:
                programming_language = 'Python'
            elif 'java' in code_file:
                programming_language = 'Java'

            if code_file == "rectangle_java2.jpg" or code_file == "rectangle_java.jpg": 
               total_tokens = 144

            elif code_file == "vehicle_java2.jpg" or code_file == "vehicle_java.jpg": 
                total_tokens = 112 
            
            elif code_file == "vehicle_python2.jpg" or code_file == "vehicle_python.jpg": 
                total_tokens = 70
            
            elif code_file == "rectangle_python2.jpg" or code_file == "rectangle_python.jpg": 
                total_tokens = 94
            
            else: 
                 raise ValueError(f"Unexpected code_file value: {code_file}")
            

            metrics = compute_metrics(data, total_tokens)

            expertise = metadata.loc[metadata['id'] == participant, 'expertise_programming'].values
            expertise_programming = expertise[0] 

            results.append({
                'Participant': participant,
                'Trial': trial,
                'code_file': code_file,
                'Programming_Language': programming_language,
                'Expertise': expertise_programming,
                'Complexity': Complexity,
                **metrics
            })


results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)
print(f"Aggregated metrics saved to {output_file}")

## No difference comparing to original version, except for appending the new column "complexity"