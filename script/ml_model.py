import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def apply_kmeans(rfm, n_clusters=3):
    """
    Apply K-Means clustering algorithm to segmented RFM data.
    """
    # Log transformation to normalize skewed data distribution
    rfm_log = np.log1p(rfm[['Recency', 'Frequency', 'Monetary']])
    
    # Standardize features to have zero mean and unit variance
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)
    
    # Initialize and fit K-Means model
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)
    
    return rfm

if __name__ == "__main__":
    # Load segment data and apply ML clustering
    rfm_data = pd.read_csv('../data/customer_segments.csv', index_col='CustomerID')
    rfm_ml = apply_kmeans(rfm_data)
    rfm_ml.to_csv('../data/rfm_with_clusters.csv')
    print("✅ Success: Machine Learning clusters assigned!")