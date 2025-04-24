import os
import pandas as pd
import matplotlib.pyplot as plt


input_dir = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Abstract_Scan_Path_Analysis/Bigram_Trigram_Results/"   
output_dir = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/semantic category analysis/trigram_plots"  
os.makedirs(output_dir, exist_ok=True)

def parse_filename(filename):
    parts = filename.replace(".txt", "").split("_")
    if len(parts) >= 4:
        return {
            "expertise": parts[2],
            "program": parts[3]  
        }
    return None

data = []

for file in os.listdir(input_dir):
    if file.startswith("trigram_expertise"):
        parsed = parse_filename(file)
        with open(os.path.join(input_dir, file), "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                if " → " in line:
                    bigram, count = line.strip().split(":")
                    data.append({
                        "trigram": bigram.strip(),
                        "count": int(count.strip()),
                        "expertise": parsed["expertise"],
                        "program": parsed["program"]
                    })

df = pd.DataFrame(data)

for (program, expertise), group in df.groupby(["program", "expertise"]):
    top_bigrams = group.sort_values("count", ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.barh(top_bigrams["trigram"], top_bigrams["count"])
    plt.xlabel("Count")
    plt.title(f"Top 10 Trigrams - {expertise.capitalize()} - {program.capitalize()}")
    plt.gca().invert_yaxis()

    filename = f"trigram_{expertise}_{program}.png"
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()