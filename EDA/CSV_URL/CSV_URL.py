#cleaning data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#CSV URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv"
#Create dataframe
df = pd.read_csv(url)
print("Original DataFrame:")
print(df)

print("\nFirst 5 rows of DataFrame:")
print(df.head())

#data info
print("\nDataFrame Info:")
print(df.info())
print("\nDataFrame Description:")
print(df.describe())
print("\nDataFrame Columns:")
print(df.columns)
print("\nDataFrame Shape:")
print(df.shape)

#data tidying
#standardize column name

df.columns = df.columns.str.strip().str.lower().str.replace(" "," ")

# handle missing or zero comsumption values
zero_consumption = df[df["consumption"] == 0]
print(zero_consumption.head())

#add derivative variables CO2 per consumption
df["co2_per_kg"] = df["co2_emmission"] / df["consumption"]
#handle division by zero
df["co2_per_kg"].fillna(0, inplace=True)

#Visualization 
plt.figure(figsize=(10,6))
sns.scatterplot(
    data = df,
    x = "consumption",
    y = "co2_emmission",
    hue = "food_category"
)
plt.title("Consumption vs CO2 Emission by Food Category")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()