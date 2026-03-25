import pandas as pd
import matplotlib as plt
df = pd.read_csv("expenses.csv")

print(df.head())
print(df.info())
print(df.describe())

#cleaning the dataset
df['Date'] = pd.to_datetime(df['Date'])
df = df.drop_duplicates()
df = df.drop(columns=['Account.1'], errors='ignore')
df = df.drop(columns=['Note.1'], errors='ignore')
df.columns = df.columns.str.strip()
print(df.isnull().sum())
print(df.head())

#for analysis purpose
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = df['Date'].dt.hour

print(df['Amount'].describe())

#Total Spending
total = df['Amount'].sum()
print("Total Spending:", total)

#Category wise spending
cat = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print(cat)

#Monthly wise trend
monthly = df.groupby('Month')['Amount'].sum()
print(df['Month'].unique())

# Creating full month index
all_months = pd.Series(range(1, 13))
monthly = monthly.reindex(all_months, fill_value=0)

print(monthly)

#Day wise spending
day = df.groupby('Day')['Amount'].sum()
print(day)

#Time of day spending
hour = df.groupby('Hour')['Amount'].sum()
print(hour)

#High Frequency Transactions
df_sorted = df.sort_values(by='Date')
df['Time_Diff'] = df['Date'].diff().dt.total_seconds() / 3600
impulse = df[df['Time_Diff'] < 2]
print("Impulse Transactions:", len(impulse))

df.to_csv("cleaned_expenses.csv", index=False)