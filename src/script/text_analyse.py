"""Text analysis helpers for NLP features."""

from pathlib import Path


RAW_DIR = Path("data/raw")
WORK_DIR = Path("data/work")


def analyze_text() -> dict:
    """Describe the text analysis artifact."""
    return {
        "text_path": str(RAW_DIR / "sample_text.txt"),
        "features_path": str(WORK_DIR / "text_features.json"),
        "status": "todo",
    }


def main() -> None:
    info = analyze_text()
    print("Text analysis ready:", info)


if __name__ == "__main__":
    main()
