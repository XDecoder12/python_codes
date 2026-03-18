import pandas as pd
df = pd.read_excel("admission data.xlsx", engine="openpyxl")
print(df.head(814))

#print(df.columns(3))

# rows, columns = df.shape
# print(f"Rows: {rows}")
# print(f"Columns: {columns}")
# print("\n")

# summary = df.describe()
# print(summary)
# print("\n")

# print(df.dtypes)
# print("\n")

# print(df[df['MQ (No.)'] < 0])
# print(df[df['MQ (%)'] < 0 ])
# print("\n")

# count = df[df['MQ (No.)'] < 0].shape[0]
# print("Number of rows where MQ is less than zero = ", count)
# print("\n")

# print(df[df['Fees'] == 0])
# count = df[df['Fees'] == 0].shape[0]
# print("Number of rows where Fees is zero = ", count)
# print("\n")

import seaborn as sns
import matplotlib.pyplot as plt

# c = 'y'
# print(sns.histplot(df['Fees'], bins=40, color=c, kde=True))
# plt.title("Distribution of Fees")
# plt.show()
# print("\n")

# correlation_matrix = df.corr(numeric_only=True)
# print(correlation_matrix)
# print(sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm'))
# plt.title("Correlation Matrix")
# plt.show()
# print("\n")

# summary = df.groupby('Type')[['Intake', 'SQ (No.)', 'Filled (No.)', 'Filled (%)']]
# summary = summary.reset_
# summary['Filled (%)'] = summary['Filled (%)'].round(2)
# print(summary)