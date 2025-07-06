# === 📌 STEP 1: Import Required Libraries ===
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# === 📁 STEP 2: Load the Dataset ===
# Use full path to avoid FileNotFoundError
file_path = "C:/Users/Jerome Yaro/Music/pollution_us_2000_2016.csv"

if os.path.exists(file_path):
    print("✅ File found!")
    df = pd.read_csv(file_path)
else:
    print("❌ File NOT found! Check path again.")
    exit()

# === 🔍 STEP 3: Select and Clean Data ===
# Keep only relevant columns
df = df[['City', 'NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']]
df.dropna(inplace=True)  # Remove rows with missing values

# === 🏙️ STEP 4: Group by City ===
# Aggregate by city to get average pollution levels
df_grouped = df.groupby('City').mean().reset_index()

# === ⚖️ STEP 5: Normalize Features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_grouped.drop(columns='City'))

# === 🧠 STEP 6: Apply K-Means Clustering ===
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df_grouped['Cluster'] = clusters

# === 🔵 STEP 7: Reduce Dimensions for Visualization (PCA) ===
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# === 📊 STEP 8: Plot the Clusters ===
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='Set2', s=60)
plt.title("City Pollution Clusters")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()

# === 🧾 STEP 9: View Sample Cities in Each Cluster ===
for i in range(k):
    print(f"\nCluster {i} sample cities:\n", df_grouped[df_grouped['Cluster'] == i]['City'].head())
