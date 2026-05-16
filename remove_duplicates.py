import pandas as pd

def remove_duplicates(input_path="data/dataset.csv", output_path="data/processed_dataset.csv"):
    df = pd.read_csv(input_path)

    df_cleaned = df.drop_duplicates()

    df_cleaned.to_csv(output_path, index=False)

    return df_cleaned

if __name__ == "__main__":
    remove_duplicates()
    print("Duplicate rows removed successfully.")
