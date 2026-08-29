import pandas as pd
import numpy as np

def clean_dataset(file_path, output_path):
    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Original Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Remove duplicate entries
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()
    
    # Fill missing numeric values with column median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())
            
    # Fill missing categorical values with column mode & trim whitespaces
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])
        df[col] = df[col].astype(str).str.strip()
        
    # Save cleaned output
    df.to_csv(output_path, index=False)
    
    print(f"Duplicates Removed: {duplicates_removed}")
    print(f"Cleaned Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Cleaned dataset saved successfully to: {output_path}")

if __name__ == "__main__":
    clean_dataset("sample_data.csv", "cleaned_output.csv")
