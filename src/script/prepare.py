"""Fusion audio+texte, split train/dev."""

import argparse
from pathlib import Path
import pandas as pd

AUDIO_PATH  = Path("data/work/audio_features.json")
TEXT_PATH   = Path("data/work/text_features.json")
OUTPUT_PATH = Path("data/work/prepared.json")
TRAIN_RATIO = 0.8


def prepare_data(
    audio_path: Path = AUDIO_PATH,
    text_path: Path = TEXT_PATH,
    output_path: Path = OUTPUT_PATH,
    train_ratio: float = TRAIN_RATIO,
) -> Path:
    # pd.merge(audio, text, on="id") -> split train/dev -> to_json(output_path)
    pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--audio", type=Path, default=AUDIO_PATH)
    p.add_argument("--text", type=Path, default=TEXT_PATH)
    p.add_argument("--output", type=Path, default=OUTPUT_PATH)
    p.add_argument("--train-ratio", type=float, default=TRAIN_RATIO)
    a = p.parse_args()
    prepare_data(a.audio, a.text, a.output, a.train_ratio)


if __name__ == "__main__":
    main()
