import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd

def generate_comparison():
    baseline = pd.read_csv("data/baseline_summary.csv")
    defense  = pd.read_csv("data/defense_summary.csv")

    baseline.columns = ["type", "similarity_before"]
    defense.columns  = ["type", "similarity_after"]

    merged = baseline.merge(defense, on="type")

    merged["improvement"] = (
        merged["similarity_after"] - merged["similarity_before"]
    ).round(4)

    merged["similarity_before"] = merged["similarity_before"].round(4)
    merged["similarity_after"]  = merged["similarity_after"].round(4)

    print("\n=== Phase 1 vs Phase 2: Defense Comparison ===")
    print(f"{'Attack Type':<25} {'Before':>8} {'After':>8} {'Gain':>8}")
    print("-" * 52)

    for _, row in merged.iterrows():
        print(
            f"{row['type']:<25} "
            f"{row['similarity_before']:>8.4f} "
            f"{row['similarity_after']:>8.4f} "
            f"{row['improvement']:>+8.4f}"
        )

    merged.to_csv("data/comparison.csv", index=False)
    print("\nSaved: data/comparison.csv")

    return merged

if __name__ == "__main__":
    generate_comparison()