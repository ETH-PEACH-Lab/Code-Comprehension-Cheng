import pandas as pd

local_metrics_file = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/local_metrics_summary.csv"
global_metrics_file = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/global_metrics_summary.csv"
output_file = "/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/all_metrics_summary.csv"

local_metrics = pd.read_csv(local_metrics_file)
global_metrics = pd.read_csv(global_metrics_file)

merged_metrics = pd.merge(
    local_metrics,
    global_metrics,
    on=["Participant", "Trial", "code_file", "Programming_Language", "Expertise"],
    how="inner"
)

merged_metrics.to_csv(output_file, index=False)

print(f"Combined metrics saved to {output_file}")

### Combine local_metrics_summary.csv and global_metrics_summary if necessary 