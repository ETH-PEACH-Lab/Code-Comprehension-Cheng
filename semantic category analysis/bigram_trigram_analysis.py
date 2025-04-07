import os
import pandas as pd
from collections import Counter
from nltk.util import ngrams

input_file = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Abstract_Scan_Path/abstract_scan_path_summary.csv"

output_dir = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Abstract_Scan_Path_Analysis/Bigram_Trigram_Results"

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_file)

def combine_code_files(name):
    if "rectangle_java" in name:
        return "rectangle_java"
    elif "vehicle_java" in name:
        return "vehicle_java"
    else:
        return None  
    
df["code_group"] = df["code_file"].apply(combine_code_files)
df = df[df["code_group"].notnull()]

def top_ngrams(scan_paths, n, top_k):
    all_ngrams = []
    for path in scan_paths:
        tokens = path.split(" → ")
        all_ngrams.extend(ngrams(tokens, n))
    return Counter(all_ngrams).most_common(top_k)

for code_group in ["rectangle_java", "vehicle_java"]:
    subset = df[df["code_group"] == code_group]
    
    for expertise_level in subset["expertise"].unique():
        group_df = subset[subset["expertise"] == expertise_level]
        scan_paths = group_df["scan_path"].tolist()
        
        bigrams = top_ngrams(scan_paths, n=2, top_k=10)
        bigram_filename = f"bigram_expertise_{expertise_level}_{code_group}.txt"
        with open(os.path.join(output_dir, bigram_filename), "w") as f:
            f.write(f"Top 10 Bigrams for expertise: {expertise_level} in {code_group}:\n")
            f.write('\n')
            for bg, count in bigrams:
                f.write(f"{' → '.join(bg)}: {count}\n")

        trigrams = top_ngrams(scan_paths, n=3, top_k=10)
        trigram_filename = f"trigram_expertise_{expertise_level}_{code_group}.txt"
        with open(os.path.join(output_dir, trigram_filename), "w") as f:
            f.write(f"Top 10 Trigrams for expertise: {expertise_level} in {code_group}:\n")
            f.write('\n')
            for tg, count in trigrams:
                f.write(f"{' → '.join(tg)}: {count}\n")