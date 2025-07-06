# ML-meets-UN-SDG
Clustering U.S. Cities by Air Quality Using Machine Learning to Support Sustainable Urban Planning (SDG 11).


 🌆 **Air Quality Watchdog – ML for SDG 11**

### 🤖 Project Summary
This project uses **Machine Learning** to cluster U.S. cities based on their average air pollution levels (NO₂, O₃, SO₂, CO), supporting **SDG 11: Sustainable Cities and Communities**.  
We apply **K-Means Clustering** to group cities by pollution profiles and visualize the clusters with **PCA**.

---

### 🌍 Sustainable Development Goal (SDG)
**SDG 11 – Sustainable Cities and Communities**  
Urban air pollution affects health, livability, and sustainability. This project helps identify the most affected cities using unsupervised learning to guide data-driven policy.

---

### 🧠 Technologies Used
- **Python**
- **pandas** – for data handling  
- **scikit-learn** – for ML (KMeans, StandardScaler, PCA)  
- **matplotlib** – for visualization  

---

### 📊 Dataset
- Source: [Kaggle – US Pollution Data (2000–2016)](https://www.kaggle.com/datasets/sogun3/uspollution)
- File: `pollution_us_2000_2016.csv` (2014 data used)
- Features used: `NO2 AQI`, `O3 AQI`, `SO2 AQI`, `CO AQI`

---

### ⚙️ How It Works
1. **Data Preprocessing**
   - Load CSV and drop missing values
   - Group by city to compute average pollution levels
   - Normalize features

2. **Clustering**
   - Apply K-Means (k = 3) to segment cities
   - Assign each city to a pollution cluster (low, medium, high)

3. **Visualization**
   - Reduce to 2D using PCA
   - Plot cities in scatter plot with cluster colors

---

### 📸 Sample Output

![Screenshot 2025-07-06 183630](https://github.com/user-attachments/assets/a4749d68-ed7a-45d3-a96d-b3e4eef0a3f3) 


---

### 🧾 Ethical Considerations
- Data only reflects U.S. cities — not globally inclusive
- Some cities may be under-monitored, skewing results
- AI should support **fair**, **sustainable**, and **non-discriminatory** outcomes

