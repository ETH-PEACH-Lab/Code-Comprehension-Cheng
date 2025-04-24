import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from scipy.stats import entropy
from sklearn.preprocessing import OneHotEncoder

input_path = "/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/Participant_Trials_Abstract_Scan_Path/abstract_scan_path_summary.csv" 
df = pd.read_csv(input_path)

def extract_custom_features(scan_path):
    tokens = scan_path.split(" → ")
    total_length = len(tokens)

    cross_transitions = sum(1 for i in range(1, len(tokens)) if tokens[i] != tokens[i-1])

    try:
        first_return_index = tokens.index("Return")
        return_position_ratio = first_return_index / total_length
    except ValueError:
        return_position_ratio = 1.0  

    bigrams = list(zip(tokens, tokens[1:]))
    bigram_counts = Counter(bigrams)
    total_bigrams = sum(bigram_counts.values())
    bigram_probs = [count / total_bigrams for count in bigram_counts.values()]
    bigram_entropy = entropy(bigram_probs, base=2) if bigram_probs else 0.0

    max_len = 1
    current_len = 1
    for i in range(1, len(tokens)):
        if tokens[i] == tokens[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return pd.Series({
        "cross_category_jumps": cross_transitions,
        "first_return_position_ratio": return_position_ratio,
        "bigram_entropy": bigram_entropy,
        "max_same_category_length": max_len,

    })

feature_df = df["scan_path"].apply(extract_custom_features)

confounders = df[["expertise", "complexity", "code_file"]].copy()

encoder = OneHotEncoder(sparse_output=False, drop="first")
confounder_encoded = pd.DataFrame(
    encoder.fit_transform(confounders),
    columns=encoder.get_feature_names_out(confounders.columns)
)

X = pd.concat([feature_df, confounder_encoded], axis=1)
y = df["Comprehension_Question_Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))