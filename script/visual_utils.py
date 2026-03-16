''''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def save_plots(df):
    """
    Generate and export key visualization charts to visuals folder.
    """
    sns.set_style("whitegrid")
    
    # Plot 1: Cluster visualization (Frequency vs Monetary)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Frequency', y='Monetary', hue='Cluster', palette='bright')
    plt.yscale('log')
    plt.title('ML Segments: Frequency vs Monetary (Log Scale)')
    plt.savefig('../visuals/cluster_scatter.png')
    plt.close()
    
    # Plot 2: Bar chart for RFM Segments
    plt.figure(figsize=(12, 6))
    df['Segment'].value_counts().plot(kind='bar', color='teal')
    plt.title('Customer Count by Rule-based Segments')
    plt.xlabel('Segments')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../visuals/segments_bar.png')
    plt.close()

if __name__ == "__main__":
    # Load final results and export visuals
    final_df = pd.read_csv('../data/rfm_with_clusters.csv')
    save_plots(final_df)
    print("✅ Success: All visuals generated in /visuals folder!")
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def export_all_visuals(data_path, output_dir='../visuals/'):
    """
    Automatically generates and saves all project charts to the visuals folder.
    """
    # 1. Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # 2. Load the final clustered data
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: {data_path} not found. Please run ml_model.py first.")
        return

    # Set general style
    sns.set_theme(style="whitegrid")
    
    # --- CHART 1: ML Clusters Scatter Plot ---
    plt.figure(figsize=(10, 7))
    sns.scatterplot(data=df, x='Frequency', y='Monetary', hue='Cluster', palette='bright', s=100, alpha=0.7)
    plt.yscale('log')
    plt.xscale('log')
    plt.title('Customer Segmentation: ML Clusters (Frequency vs Monetary)', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'cluster_scatter.png'), dpi=300)
    plt.close()
    print("✅ Saved: cluster_scatter.png")

    # --- CHART 2: Traditional RFM Segments Bar Chart ---
    plt.figure(figsize=(12, 6))
    segment_order = df['Segment'].value_counts().index
    sns.countplot(data=df, y='Segment', order=segment_order, palette='viridis')
    plt.title('Customer Distribution by Traditional RFM Segments', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'segments_bar.png'), dpi=300)
    plt.close()
    print("✅ Saved: segments_bar.png")

    # --- CHART 3: Recency Boxplot by Cluster ---
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Cluster', y='Recency', data=df, palette='bright')
    plt.title('Recency Distribution across ML Clusters', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'recency_boxplot.png'), dpi=300)
    plt.close()
    print("✅ Saved: recency_boxplot.png")

    # --- CHART 4: Revenue Share Pie Chart ---
    plt.figure(figsize=(10, 8))
    # Grouping by our business names if available, else by Cluster
    group_col = 'Cluster_Name' if 'Cluster_Name' in df.columns else 'Cluster'
    revenue_share = df.groupby(group_col)['Monetary'].sum()
    
    plt.pie(revenue_share, labels=revenue_share.index, autopct='%1.1f%%', 
            colors=sns.color_palette('pastel'), startangle=140, explode=[0.05]*len(revenue_share))
    plt.title('Total Revenue Contribution by Segment', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'revenue_pie_chart.png'), dpi=300)
    plt.close()
    print("✅ Saved: revenue_pie_chart.png")

    print("\n🚀 All visuals have been successfully exported to the /visuals/ folder!")

if __name__ == "__main__":
    # Path to the data generated in the previous step
    data_file = '../data/final_customer_insights.csv'
    export_all_visuals(data_file)
    '''
# --- CHART 5: Frequency vs Recency Scatter (Activity Pattern) ---
    plt.figure(figsize=(10, 7))
    sns.scatterplot(data=df, x='Recency', y='Frequency', hue='Cluster_Name', palette='bright', s=80)
    plt.title('Activity Pattern: How often vs How recently', fontsize=14)
    plt.savefig(os.path.join(output_dir, '05_frequency_vs_recency.png'), dpi=300)
    plt.close()
    print("✅ Saved: 05_frequency_vs_recency.png")

    # --- CHART 6: Monetary Value Distribution (Violin Plot) ---
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='Cluster_Name', y='Monetary', data=df, palette='pastel')
    plt.yscale('log')
    plt.title('Monetary Value Density by Segment', fontsize=14)
    plt.savefig(os.path.join(output_dir, '06_monetary_density.png'), dpi=300)
    plt.close()
    print("✅ Saved: 06_monetary_density.png")

    # --- CHART 7: Average RFM Scores (Radar/Spider Chart alternative) ---
    plt.figure(figsize=(10, 6))
    avg_rfm = df.groupby('Cluster_Name')[['Recency', 'Frequency', 'Monetary']].mean()
    # Normalize for better visualization in bar chart
    avg_rfm_norm = (avg_rfm - avg_rfm.min()) / (avg_rfm.max() - avg_rfm.min())
    avg_rfm_norm.plot(kind='bar', figsize=(12,6), colormap='viridis')
    plt.title('Comparison of Normalized RFM Metrics across Segments', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(output_dir, '07_segment_comparison.png'), dpi=300)
    plt.close()
    print("✅ Saved: 07_segment_comparison.png")

    # --- CHART 8: Frequency Distribution (Histogram) ---
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Frequency'], bins=50, kde=True, color='purple')
    plt.xlim(0, df['Frequency'].quantile(0.95)) # Focus on the bulk of customers
    plt.title('Overall Purchase Frequency Distribution', fontsize=14)
    plt.savefig(os.path.join(output_dir, '08_frequency_histogram.png'), dpi=300)
    plt.close()
    print("✅ Saved: 08_frequency_histogram.png")