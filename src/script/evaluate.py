"""Evaluation du classifieur sur le jeu de dev."""

import argparse
from pathlib import Path
import pandas as pd

PREPARED_PATH = Path("data/work/prepared.json")
MODEL_PATH    = Path("data/work/model")
OUTPUT_PATH   = Path("data/work/evaluation.json")


def evaluate_model(prepared_path: Path = PREPARED_PATH, model_path: Path = MODEL_PATH, output_path: Path = OUTPUT_PATH) -> Path:
    # spacy.load(model_path) -> predict sur dev -> accuracy/F1/confusion -> to_json(output_path)
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prepared", type=Path, default=PREPARED_PATH)
    p.add_argument("--model", type=Path, default=MODEL_PATH)
    p.add_argument("--output", type=Path, default=OUTPUT_PATH)
    a = p.parse_args()
    evaluate_model(a.prepared, a.model, a.output)


if __name__ == "__main__":
    main()
