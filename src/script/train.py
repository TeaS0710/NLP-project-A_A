"""Training step for the baseline ML model."""

from pathlib import Path


WORK_DIR = Path("data/work")


def train_model() -> dict:
    """Return the expected training contract."""
    return {
        "dataset_path": str(WORK_DIR / "prepared.json"),
        "model_path": str(WORK_DIR / "model.joblib"),
        "status": "todo",
    }


def main() -> None:
    info = train_model()
    print("Training ready:", info)


if __name__ == "__main__":
    main()
