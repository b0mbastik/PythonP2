import pandas as pd
import os

def read_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError("Error: census2011.csv not found in the correct directory.")

def refine_dataset(df):
    df = df.drop_duplicates()

    categorical_columns = ['Region', 'Residence Type', 'Family Composition', 'Population Base', 'Sex', 'Marital Status', 'Student', 'Country of Birth', 'Health', 'Ethnic Group', 'Religion', 'Economic Activity', 'Occupation', 'Industry', 'Approximated Social Grade']
    for column in categorical_columns:
        df[column] = df[column].astype('category')

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Hours worked per week'] = pd.to_numeric(df['Hours worked per week'], errors='coerce')

    df = df[df['Age'] >= 0]

    return df

def save_refined_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == '__main__': # pragma: no cover
    file_path = 'census2011.csv'
    refined_file_path = 'refined_census2011.csv'
    df = read_data(file_path)
    refined_df = refine_dataset(df)
    save_refined_data(refined_df, refined_file_path)
    print(f"Refined dataset saved to {refined_file_path}.")

    df = pd.read_csv('refined_census2011.csv')
    total_records = len(df)
    print("Total number of records:", total_records)