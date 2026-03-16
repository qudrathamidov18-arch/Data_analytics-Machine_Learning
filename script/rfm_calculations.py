import pandas as pd
import datetime as dt

def calculate_rfm(df):
    """
    Calculate Recency, Frequency, and Monetary metrics per customer.
    """
    # Define reference date as the day after the last transaction
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    
    # Aggregate data by CustomerID
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'count',
        'TotalSum': 'sum'
    })
    
    # Rename columns for clarity
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm

def assign_segments(rfm):
    """
    Assign scores and business segments based on RFM values.
    """
    # Score metrics from 1 to 5 (Recency: lower is better)
    rfm['R'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
    
    # Define mapping for customer behavior segments
    seg_map = {
        r'[1-2][1-2]': 'Hibernating',
        r'[1-2][3-4]': 'At Risk',
        r'[1-2]5': 'Can\'t Loose Them',
        r'3[1-2]': 'About to Sleep',
        r'33': 'Need Attention',
        r'[3-4][4-5]': 'Loyal Customers',
        r'41': 'Promising',
        r'51': 'New Customers',
        r'[4-5][2-3]': 'Potential Loyalists',
        r'5[4-5]': 'Champions'
    }
    
    # Create segment column by combining R and F scores
    rfm['Segment'] = rfm['R'].astype(str) + rfm['F'].astype(str)
    rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
    return rfm

if __name__ == "__main__":
    # Load processed data and calculate RFM
    df = pd.read_csv('../data/processed_retail.csv', parse_dates=['InvoiceDate'])
    rfm_table = calculate_rfm(df)
    rfm_final = assign_segments(rfm_table)
    rfm_final.to_csv('../data/customer_segments.csv')
    print("✅ Success: RFM metrics and rule-based segments are ready!")