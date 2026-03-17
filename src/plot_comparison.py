import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # headless, safe for CI

def plot_comparison():
    df = pd.read_csv("data/comparison.csv")

    attack_labels = {
        "emoji_insertion":   "Emoji\nInsertion",
        "emoji_replacement": "Emoji\nReplacement",
        "unicode":           "Unicode\nSubstitution",
        "whitespace":        "Whitespace\nPerturbation"
    }

    labels = [attack_labels.get(t, t) for t in df["type"]]
    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    bars_before = ax.bar(
        [i - width/2 for i in x],
        df["similarity_before"], width,
        label="Before sanitization", color="#d9534f", alpha=0.85
    )
    bars_after = ax.bar(
        [i + width/2 for i in x],
        df["similarity_after"], width,
        label="After sanitization", color="#5cb85c", alpha=0.85
    )

    # Value labels on bars
    for bar in bars_before:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{bar.get_height():.3f}",
            ha="center", va="bottom", fontsize=8
        )
    for bar in bars_after:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{bar.get_height():.3f}",
            ha="center", va="bottom", fontsize=8
        )

    ax.set_xlabel("Attack Type", fontsize=11)
    ax.set_ylabel("Average Cosine Similarity", fontsize=11)
    ax.set_title(
        "Embedding Similarity: Before vs After Sanitization Defense",
        fontsize=12
    )
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 1.1)
    ax.axhline(y=1.0, color="gray", linestyle="--", alpha=0.4, linewidth=0.8)
    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.savefig("data/comparison_plot.png", dpi=150)
    print("Saved: data/comparison_plot.png")

if __name__ == "__main__":
    plot_comparison()