from pathlib import Path
import argparse

import pandas as pd
from datasets import load_dataset


DATASET_NAME = "AnkitAI/product-reviews-sentiment"

OUTPUT_DIR = Path("data")
OUTPUT_FILE = OUTPUT_DIR / "reviews.csv"


def download_reviews(
    output_file: Path = OUTPUT_FILE,
    sample_size: int = 100,
) -> None:
    """
    Download a sample of customer reviews from Hugging Face
    and save them as a local CSV file.
    """

    print(f"Loading dataset: {DATASET_NAME}")

    dataset = load_dataset(
        DATASET_NAME,
        split="train",
    )

    print(f"Dataset loaded: {len(dataset):,} rows")

    sample_size = min(sample_size, len(dataset))

    dataset = dataset.shuffle(seed=42).select(
        range(sample_size)
    )

    df = dataset.to_pandas()

    # Keep only the fields needed by V1.
    df = df[["review", "category"]].copy()

    # Add our own stable local ID.
    df.insert(
        0,
        "review_id",
        range(1, len(df) + 1),
    )

    # Remove empty reviews.
    df["review"] = df["review"].fillna("").astype(str)

    df = df[
        df["review"].str.strip() != ""
    ].copy()

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        output_file,
        index=False,
    )

    print(
        f"Saved {len(df):,} reviews to {output_file}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download customer review dataset."
    )

    parser.add_argument(
        "--sample-size",
        type=int,
        default=1000,
        help="Number of reviews to download.",
    )

    args = parser.parse_args()

    download_reviews(
        sample_size=args.sample_size
    )


if __name__ == "__main__":
    main()