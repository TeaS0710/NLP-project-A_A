"""Evaluate : teste le modele sur le dev set."""

import json
from pathlib import Path

import spacy


def main():
    with open("data/work/prepared.json", encoding="utf-8") as f:
        data = json.load(f)

    nlp = spacy.load("data/work/model")

    correct = 0
    total = len(data["dev"])

    print(f"\n{'ID':<15} {'GOLD':<10} {'PRED':<10} {'HEALTHY':>8} {'SICK':>8}")
    print("-" * 55)

    for ex in data["dev"]:
        doc = nlp(ex["text"])
        pred = max(doc.cats, key=doc.cats.get)
        gold = ex["label"]
        if pred == gold:
            correct += 1
        print(f"{ex['id']:<15} {gold:<10} {pred:<10} "
              f"{doc.cats['HEALTHY']:>8.4f} {doc.cats['SICK']:>8.4f}")

    acc = correct / total if total else 0
    print(f"\n[evaluate] accuracy={acc:.2%} ({correct}/{total})")

    result = {"accuracy": round(acc, 4), "correct": correct, "total": total}
    with open("data/work/evaluation.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"[evaluate] -> data/work/evaluation.json")


if __name__ == "__main__":
    main()
