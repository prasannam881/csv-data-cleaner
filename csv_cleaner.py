import pandas as pd

def clean_csv(file_path, output_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.to_csv(output_path, index=False)
    print("CSV cleaned and saved at", output_path)

# Example usage
clean_csv('input.csv', 'cleaned.csv')
