#cleaning data
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Region": ["North", "South", "East", "West", "Central"],
    "Product": ["A", "B", "C", "D", "E"],
    "January_Sales": [250, 150, 567, 300, 200],
    "February_Sales": [200, 234, 250, 350, 300],
    "March_Sales": [300, 200, 400, None, 250]
}

#Create dataframe
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#Tidying Data 
#Identify identifier and measured variables
# Identifier : Region, Product
# Measured : January_Sales, February_Sales, March_Sales
# Measure variables : January_Sales, February_Sales, March_Sales
# Convert the columns into rows using melt function

tidy_df = pd.melt(
    df,
    id_vars=["Region", "Product"],
    value_vars=["January_Sales", "February_Sales", "March_Sales"],
    var_name="Month",
    value_name="Sales"
)
print("\nTidy DataFrame:")
print(tidy_df)

# clean data
tidy_df['Month'] = tidy_df['Month'].str.replace('_Sales', '')
print("\nCleaned Tidy DataFrame:")
print(tidy_df)

# Example plot to visualize the tidy data
plt.bar(tidy_df['Month'], tidy_df['Sales'])
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.show()

# Example plot to visualize the tidy data
plt.plot(tidy_df['Product'], tidy_df['Sales'], marker='o')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Monthly Sales Data Line Plot')
plt.show()