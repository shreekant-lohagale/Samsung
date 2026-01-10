'''Create a dataframe: Name : jaya, vinay, tina, gana, Era. Age : 23, 25, 15, 13, 21
- create a dataframe using above data
- show the names who are appliable for voting (age >= 18)
- except tina display the dataframe
- add one columnm 'city' in dataframe
- display who's clty is not equal to pune
- display the only name which start with 'G'
- print only top 3 rows
- print only last 2 rows
- display the data whose city name started with 'M' '''
import pandas as pd
data = {
    'Name': ['jaya', 'vinay', 'tina', 'gana', 'Era'],
    'Age': [23, 25, 15, 13, 21]
}
df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

# Show names who are applicable for voting (age >= 18)
voting_eligible = df[df['Age'] >= 18]
print("Names eligible for voting:")
print(voting_eligible)

# Except tina display the dataframe
df_except_tina = df[df['Name'] != 'tina']
print("\nDataFrame except tina:")
print(df_except_tina)

# Add one column 'city' in dataframe
df['City'] = ['Mumbai', 'Pune', 'Delhi', 'Chennai', 'Mumbai']
print("\nDataFrame with city column added:")    
print(df)

# Display whose city is not equal to pune
not_pune = df[df['City'] != 'Pune']
print("\nDataFrame where city is not Pune:")
print(not_pune)

# Display only name which starts with 'G'
starts_with_g = df[df['Name'].str.startswith('g')]
print("\nNames starting with 'G':")
print(starts_with_g)

# Print only top 3 rows
top_3_rows = df.head(3)
print("\nTop 3 rows:")  
print(top_3_rows)

# Print only last 2 rows        
last_2_rows = df.tail(2)
print("\nLast 2 rows:")
print(last_2_rows)

# Display the data whose city name started with 'M'
city_starts_with_m = df[df['City'].str.startswith('M')]
print("\nData where city starts with 'M':")
print(city_starts_with_m)
