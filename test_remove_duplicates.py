import pandas as pd
from remove_duplicates import remove_duplicates

def test_duplicates_removed():
    remove_duplicates("data/dataset.csv", "data/processed_dataset.csv")
    processed = pd.read_csv("data/processed_dataset.csv")
    assert processed.duplicated().sum() == 0

def test_processed_rows_not_more_than_original():
    original = pd.read_csv("data/dataset.csv")
    processed = pd.read_csv("data/processed_dataset.csv")
    assert len(processed) <= len(original)
