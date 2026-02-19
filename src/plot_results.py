import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/baseline_results.csv")

plt.figure()
plt.bar(df["type"], df["similarity"])
plt.xlabel("Attack Type")
plt.ylabel("Average Cosine Similarity")
plt.title("Embedding Similarity Under Surface-Level Attacks")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("data/baseline_plot.png")
plt.show()
