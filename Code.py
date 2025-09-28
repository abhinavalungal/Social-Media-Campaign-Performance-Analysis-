import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("KAG_conversion_data.csv")

# =====================
# BASIC EXPLORATION
# =====================
print("\n--- Head ---")
print(df.head())
print("\n--- Info ---")
print(df.info())
print("\n--- Describe ---")
print(df.describe())
print("\n--- Missing Values ---")
print(df.isnull().sum())

# =====================
# FEATURE ENGINEERING
# =====================
df["ConversionRate"] = df["Approved_Conversion"] / df["Impressions"]
df["CTR"] = df["Clicks"] / df["Impressions"]
df["CPC"] = df["Spent"] / (df["Clicks"].replace(0, 1))  # Cost per click
df["CPA"] = df["Spent"] / (df["Approved_Conversion"].replace(0, 1))  # Cost per acquisition

# =====================
# CORRELATION ANALYSIS
# =====================
plt.figure(figsize=(8, 6))
sns.heatmap(
    df[["Impressions","Clicks","Spent","Total_Conversion","Approved_Conversion","CTR","ConversionRate","CPC","CPA"]].corr(),
    annot=True, fmt=".2f", cmap="coolwarm"
)
plt.title("Correlation Heatmap of Campaign Metrics")
plt.show()

# =====================
# DISTRIBUTIONS
# =====================
for col in ["CTR", "ConversionRate", "CPC", "CPA"]:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# =====================
# RELATIONSHIPS
# =====================
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Impressions", y="Clicks", data=df, alpha=0.6)
plt.title("Impressions vs Clicks")
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x="Spent", y="Approved_Conversion", data=df, alpha=0.6)
plt.title("Spent vs Approved Conversions")
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x="Spent", y="CTR", data=df, alpha=0.6)
plt.title("Spend vs CTR")
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x="Spent", y="ConversionRate", data=df, alpha=0.6)
plt.title("Spend vs Conversion Rate")
plt.show()

# =====================
# CAMPAIGN COMPARISON
# =====================
if "campaign" in df.columns:
    campaign_summary = df.groupby("campaign")[["CTR","ConversionRate","CPC","CPA"]].mean().reset_index()
    print("\n--- Campaign Summary ---")
    print(campaign_summary)

    for metric in ["CTR", "ConversionRate", "CPC", "CPA"]:
        plt.figure(figsize=(6, 4))
        sns.barplot(x="campaign", y=metric, data=campaign_summary)
        plt.title(f"{metric} by Campaign")
        plt.show()

# =====================
# TIME-SERIES ANALYSIS
# =====================
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
    daily = df.groupby("date")[["Impressions","Clicks","Spent","Approved_Conversion","CTR","ConversionRate"]].mean().reset_index()

    for metric in ["Impressions", "Clicks", "Spent", "Approved_Conversion", "CTR", "ConversionRate"]:
        plt.figure(figsize=(8, 4))
        sns.lineplot(x="date", y=metric, data=daily)
        plt.title(f"Daily Trend of {metric}")
        plt.xlabel("Date")
        plt.ylabel(metric)
        plt.show()

