"""Entrainement classifieur binaire spaCy textcat (OUI=1 / NON=0)."""

import argparse
from pathlib import Path
import pandas as pd

PREPARED_PATH = Path("data/work/prepared.json")
MODEL_PATH    = Path("data/work/model")
N_ITER        = 20


def train_model(prepared_path: Path = PREPARED_PATH, model_path: Path = MODEL_PATH, n_iter: int = N_ITER) -> Path:
    # spacy.blank + textcat(OUI/NON) -> nlp.initialize + nlp.update x n_iter -> nlp.to_disk
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prepared", type=Path, default=PREPARED_PATH)
    p.add_argument("--model", type=Path, default=MODEL_PATH)
    p.add_argument("--n-iter", type=int, default=N_ITER)
    a = p.parse_args()
    train_model(a.prepared, a.model, a.n_iter)


if __name__ == "__main__":
    main()
