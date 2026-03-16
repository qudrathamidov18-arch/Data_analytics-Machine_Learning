import pandas as pd

def clean_data(filepath):
    """
    Load raw data and perform basic cleaning operations.
    """
    # Load dataset with specific encoding for retail data
    df = pd.read_csv(filepath, encoding="ISO-8859-1")
    
    # Remove rows where CustomerID is missing
    df.dropna(subset=['CustomerID'], inplace=True)
    
    # Convert InvoiceDate to datetime objects
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Filter out invalid transactions (negative or zero quantities/prices)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    
    # Calculate Total Revenue per transaction
    df['TotalSum'] = df['Quantity'] * df['UnitPrice']
    
    return df

if __name__ == "__main__":
    # Execute cleaning process
    df_cleaned = clean_data('../data/raw_data.csv')
    df_cleaned.to_csv('../data/processed_retail.csv', index=False)
    print("✅ Success: Data cleaning completed and saved to processed_retail.csv")