"""Evaluation step for metrics and validation."""

from pathlib import Path


WORK_DIR = Path("data/work")


def evaluate_model() -> dict:
    """Return the expected evaluation outputs."""
    return {
        "model_path": str(WORK_DIR / "model.joblib"),
        "report_path": str(WORK_DIR / "evaluation.json"),
        "status": "todo",
    }


def main() -> None:
    info = evaluate_model()
    print("Evaluation ready:", info)


if __name__ == "__main__":
    main()
