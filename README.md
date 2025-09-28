## Social-Media-Campaign-Performance-Analysis

## Project Overview
This project analyzes a campaign clicks and conversions dataset to understand user behavior, campaign performance, and factors affecting conversions. The goal is to generate insights using visualizations and build a predictive model for total conversions.

## Dataset
- **Source:** Kaggle (`KAG_conversion_data.csv`)
- **Features include:**  
  - `xyz_campaign_id` – Campaign identifier  
  - `fb_campaign_id` – Facebook campaign identifier  
  - `Impressions` – Number of ad impressions  
  - `Clicks` – Number of clicks received  
  - `Spent` – Ad spend amount  
  - `Total_Conversion` – Total conversions  
  - `Approved_Conversion` – Approved conversions  
  - `age` – User age  
  - `gender` – User gender  
  - `interest` – User interest category  

## Libraries Used
- `pandas`, `numpy` – Data manipulation  
- `matplotlib`, `seaborn` – Data visualization  
- `scikit-learn` – Preprocessing, model training, and evaluation  

## Analysis Conducted
- Exploratory Data Analysis (EDA)  
  - Checked null values, dataset shape, and summary statistics  
  - Correlation heatmap  
  - Countplots and barplots for campaigns, age, gender, and interests  
  - Scatterplots and FacetGrids to visualize relationships between features and approved conversions  
- Campaign-specific analysis (e.g., campaign_c)  
- Feature encoding for categorical variables  
- Feature scaling for model training  

## Predictive Modeling
- **Model:** Random Forest Regressor  
- **Target Variable:** `Total_Conversion`  
- **Metrics Used:**  
  - Mean Absolute Error (MAE)  
  - Root Mean Squared Error (RMSE)  
  - R² Score  

## Results
- The model predicts total conversions based on campaign and user data.  
- Visualizations provide insights into which campaigns, demographics, and interests drive approved conversions.  

## Usage
1. Clone the repository.  
2. Install required libraries:  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
