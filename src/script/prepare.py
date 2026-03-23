"""Preparation step for feature building and cleaning."""

from pathlib import Path


WORK_DIR = Path("data/work")


def prepare_data() -> dict:
    """Describe the prepared dataset artifact."""
    return {
        "input_path": str(WORK_DIR / "extracted.json"),
        "output_path": str(WORK_DIR / "prepared.json"),
        "status": "todo",
    }


def main() -> None:
    info = prepare_data()
    print("Preparation ready:", info)


if __name__ == "__main__":
    main()
