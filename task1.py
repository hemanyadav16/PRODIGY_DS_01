import pandas as pd

# Load the dataset (adjust path if needed)
df = pd.read_csv(r'C:\Users\yadav\OneDrive\Desktop\prodigy\API_SP.POP.TOTL_DS2_en_csv_v2_19373\API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv', skiprows=4)

# View structure
print(df.head())
df = df[['Country Name', '2022']]
df.columns = ['Country', 'Population']
df = df.dropna()
import matplotlib.pyplot as plt

# Top 10 most populous countries
top_10 = df.sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10['Country'], top_10['Population'], color='skyblue')
plt.title('Top 10 Most Populous Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
