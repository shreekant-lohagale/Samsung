import pandas as pd
import matplotlib.pyplot as plt

# ---------------- NATIONAL LEVEL ANALYSIS ---------------- #

nation = pd.read_csv(r"E:\Samsung\project\mini-projects\nation_level_daily.csv")

nation['Date'] = nation['Date'].astype(str) + " 2020"
nation['Date'] = pd.to_datetime(nation['Date'], format="%d %B %Y")

print("Nation Level Dataset Info:")
print(nation.info())
print(nation.head())

plt.figure()
plt.plot(nation['Date'], nation['Total Confirmed'], label='Total Confirmed')
plt.plot(nation['Date'], nation['Total Recovered'], label='Total Recovered')
plt.plot(nation['Date'], nation['Total Deceased'], label='Total Deceased')
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.title("India COVID-19 National Trend")
plt.legend()
plt.show()


# ---------------- STATE LEVEL ANALYSIS ---------------- #

state = pd.read_csv(r"E:\Samsung\project\mini-projects\state_level_latest.csv")

top_states = state.sort_values(by='Confirmed', ascending=False).head(10)

plt.figure()
plt.bar(top_states['State'], top_states['Confirmed'])
plt.xticks(rotation=45)
plt.xlabel("State")
plt.ylabel("Confirmed Cases")
plt.title("Top 10 States by COVID-19 Cases")
plt.show()


# ---------------- TESTING ANALYSIS ---------------- #

tests = pd.read_csv(r"E:\Samsung\project\mini-projects\tests_day_wise.csv")

print("Testing dataset columns:", tests.columns)

# CORRECT column names
tests['Date'] = pd.to_datetime(tests['Tested As Of'])

plt.figure()
plt.plot(tests['Date'], tests['Total Samples Tested'], label='Total Tests')
plt.xlabel("Date")
plt.ylabel("Number of Tests")
plt.title("COVID-19 Testing Trend in India")
plt.legend()
plt.show()
