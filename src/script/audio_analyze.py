"""Analyse audio avec wav2vec2."""

import argparse
from pathlib import Path
import pandas as pd

CORPUS_PATH = Path("data/corpus/sample_corpus.json")
OUTPUT_PATH = Path("data/work/audio_features.json")


def analyze_audio(corpus_path: Path = CORPUS_PATH, output_path: Path = OUTPUT_PATH) -> Path:
    # pd.read_json(corpus_path) -> librosa + Wav2Vec2 (mean pooling) -> df.to_json(output_path)
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--corpus", type=Path, default=CORPUS_PATH)
    p.add_argument("--output", type=Path, default=OUTPUT_PATH)
    a = p.parse_args()
    analyze_audio(a.corpus, a.output)


if __name__ == "__main__":
    main()
