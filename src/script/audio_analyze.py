"""Audio analysis helpers for signal-level features."""

from pathlib import Path


RAW_DIR = Path("data/raw")
WORK_DIR = Path("data/work")


def analyze_audio() -> dict:
    """Describe the audio analysis artifact."""
    return {
        "audio_path": str(RAW_DIR / "sample_audio.mp3"),
        "features_path": str(WORK_DIR / "audio_features.json"),
        "status": "todo",
    }


def main() -> None:
    info = analyze_audio()
    print("Audio analysis ready:", info)


if __name__ == "__main__":
    main()
