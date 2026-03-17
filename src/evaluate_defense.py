import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
from src.sanitization import sanitize

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)
model.eval()

def get_embedding(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
        padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def evaluate_with_defense(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for _, row in df.iterrows():
        sanitized = sanitize(row["adversarial"])

        emb_clean = get_embedding(row["clean"])
        emb_sanitized = get_embedding(sanitized)

        similarity = cosine_similarity(emb_clean, emb_sanitized)[0][0]

        rows.append({
            "type": row["type"],
            "clean": row["clean"],
            "adversarial": row["adversarial"],
            "sanitized": sanitized,
            "similarity_after": float(similarity)
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = pd.read_csv("data/adversarial_prompts.csv")

    results = evaluate_with_defense(df)

    summary = results.groupby("type")["similarity_after"].mean().reset_index()

    print("\n=== Phase 2: After Sanitization Defense ===")
    print(summary.to_string(index=False))

    results.to_csv("data/defense_results.csv", index=False)
    summary.to_csv("data/defense_summary.csv", index=False)

    print("\nSaved: data/defense_results.csv and data/defense_summary.csv")