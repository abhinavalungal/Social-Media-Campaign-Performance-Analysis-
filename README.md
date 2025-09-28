<h1 align="center">Social Media Campaign Performance Analysis </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## Project Overview  
This project analyzes **social media ad campaigns** to optimize **sales conversion** and predict **total conversions**.  
It is built in **Python** and uses a **Random Forest Regressor** to forecast conversions based on ad performance metrics and user demographics.  

## Features  
- Uses a **social media ad campaign dataset** with 11 features  
- Performs **data preprocessing**, **EDA**, and correlation analysis  
- Visualizes **campaign performance**, **age & gender distribution**, and **interest impact**  
- Encodes categorical variables for **machine learning modeling**  
- Trains a **Random Forest Regressor** to predict `Total_Conversion`  
- Evaluates model using **MAE, RMSE, and R² Score**  
- Provides insights for **campaign optimization** and **target audience selection**  

---

## Tech Stack  
- Python  
- NumPy  
- Pandas  
- Matplotlib & Seaborn  
- scikit-learn (sklearn)  

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
