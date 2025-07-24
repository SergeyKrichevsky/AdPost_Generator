# evaluation/view_results.py

import pandas as pd

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "results.csv")

def display_results(csv_path, num_rows=50):
    """
    Load and display evaluation results as a DataFrame.

    Parameters:
    - csv_path (str): Path to the CSV results file.
    - num_rows (int): Number of rows to display (default = 50)
    """
    df = pd.read_csv(csv_path)

    print("\n📊 Evaluation Results Overview:\n")
    print(df.head(num_rows))

    print("\n📈 Summary Statistics:\n")
    print(df.describe(include='all'))

if __name__ == "__main__":
    display_results(csv_path)
