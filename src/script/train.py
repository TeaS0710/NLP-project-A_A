"""Train : textcat spaCy binaire HEALTHY vs SICK."""

import json
import random
from pathlib import Path

import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding


def main():
    with open("data/work/prepared.json", encoding="utf-8") as f:
        data = json.load(f)

    nlp = spacy.blank("en")
    textcat = nlp.add_pipe("textcat")
    textcat.add_label("HEALTHY")
    textcat.add_label("SICK")

    train_examples = [
        Example.from_dict(nlp.make_doc(ex["text"]), {"cats": ex["cats"]})
        for ex in data["train"]
    ]

    nlp.initialize(get_examples=lambda: train_examples)

    random.seed(42)
    for i in range(20):
        random.shuffle(train_examples)
        losses = {}
        for batch in minibatch(train_examples, size=compounding(4.0, 32.0, 1.001)):
            nlp.update(batch, losses=losses)
        print(f"[train] iter {i+1:>2}/20  loss={losses['textcat']:.4f}")

    Path("data/work/model").mkdir(parents=True, exist_ok=True)
    nlp.to_disk("data/work/model")
    print("[train] modele -> data/work/model")


if __name__ == "__main__":
    main()
