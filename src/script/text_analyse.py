"""Analyse texte avec spaCy."""

import argparse
from pathlib import Path
import pandas as pd

CORPUS_PATH = Path("data/corpus/sample_corpus.json")
OUTPUT_PATH = Path("data/work/text_features.json")
SPACY_MODEL = "fr_core_news_md"


def analyze_text(corpus_path: Path = CORPUS_PATH, output_path: Path = OUTPUT_PATH, model: str = SPACY_MODEL) -> Path:
    # pd.read_json(corpus_path) -> spacy.load(model) -> doc.vector + n_tokens -> df.to_json(output_path)
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--corpus", type=Path, default=CORPUS_PATH)
    p.add_argument("--output", type=Path, default=OUTPUT_PATH)
    p.add_argument("--model", type=str, default=SPACY_MODEL)
    a = p.parse_args()
    analyze_text(a.corpus, a.output, a.model)


if __name__ == "__main__":
    main()
