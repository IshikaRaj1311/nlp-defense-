import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_comparison():
    df = pd.read_csv("data/comparison.csv")

    attack_labels = {
        "emoji_insertion": "Emoji\nInsertion",
        "emoji_replacement": "Emoji\nReplacement",
        "unicode": "Unicode\nSubstitution",
        "whitespace": "Whitespace\nPerturbation"
    }

    labels = [attack_labels.get(t, t) for t in df["type"]]
    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))

    bars_before = ax.bar(
        [i - width/2 for i in x],
        df["similarity_before"], width,
        label="Before"
    )

    bars_after = ax.bar(
        [i + width/2 for i in x],
        df["similarity_after"], width,
        label="After"
    )

    ax.set_xlabel("Attack Type")
    ax.set_ylabel("Average Cosine Similarity")
    ax.set_title("Before vs After Sanitization Defense")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.1)
    ax.legend()

    plt.tight_layout()
    plt.savefig("data/comparison_plot.png", dpi=150)

    print("Saved: data/comparison_plot.png")

if __name__ == "__main__":
    plot_comparison()