"""Extraction step for raw corpus ingestion."""

from pathlib import Path


RAW_DIR = Path("data/raw")
WORK_DIR = Path("data/work")


def extract_data() -> dict:
    """Collect input file locations for downstream processing."""
    return {
        "audio_path": str(RAW_DIR / "sample_audio.mp3"),
        "text_path": str(RAW_DIR / "sample_text.txt"),
        "output_path": str(WORK_DIR / "extracted.json"),
    }


def main() -> None:
    info = extract_data()
    print("Extraction ready:", info)


if __name__ == "__main__":
    main()
