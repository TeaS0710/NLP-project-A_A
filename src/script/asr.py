"""ASR entrypoint for speech-to-text experiments."""

from pathlib import Path


RAW_DIR = Path("data/raw")
WORK_DIR = Path("data/work")


def run_asr() -> dict:
    """Define the ASR I/O contract."""
    return {
        "audio_path": str(RAW_DIR / "sample_audio.mp3"),
        "transcript_path": str(WORK_DIR / "asr_transcript.json"),
        "status": "todo",
    }


def main() -> None:
    info = run_asr()
    print("ASR ready:", info)


if __name__ == "__main__":
    main()
