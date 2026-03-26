"""Prepare : charge les corpus healthy/sick, nettoie, split train/dev."""

import json
import random
import re
from pathlib import Path


def clean(text):
    """Nettoie une utterance CLAN."""
    text = re.sub(r"\x15\d+_\d+\x15", "", text)
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&-\w+", "", text)
    text = re.sub(r"\+<?\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def load_corpus(path, label):
    """Charge un corpus JSON et retourne une liste de {text, cats}."""
    with open(path, encoding="utf-8") as f:
        docs = json.load(f)["documents"]

    examples = []
    for doc in docs:
        text = " ".join(
            clean(u["text"]) for u in doc["utterances"] if u["speaker"] == "PAR"
        ).strip()
        if text:
            examples.append({
                "id": doc["filename"],
                "text": text,
                "label": label,
                "cats": {"HEALTHY": float(label == "HEALTHY"),
                         "SICK":    float(label == "SICK")},
            })
    return examples


def main():
    healthy = load_corpus("data/raw/corpus_healthy.json", "HEALTHY")
    sick = load_corpus("data/raw/corpus_sick.json", "SICK")
    data = healthy + sick

    random.seed(42)
    random.shuffle(data)
    split = int(len(data) * 0.8)

    out = {"train": data[:split], "dev": data[split:],
           "meta": {"labels": ["HEALTHY", "SICK"], "train": split, "dev": len(data) - split}}

    Path("data/work").mkdir(parents=True, exist_ok=True)
    with open("data/work/prepared.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"[prepare] train={split} dev={len(data) - split} total={len(data)}")


if __name__ == "__main__":
    main()
