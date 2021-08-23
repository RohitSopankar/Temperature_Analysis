import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

df = pd.read_csv('weatherHistory.csv')
df.head()

df.shape
df.dtypes
df.isnull().sum()

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df = df.set_index("Formatted Date")
df.head(2)

data_columns = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df[data_columns].resample('MS').mean()
df_monthly_mean.head()

data_columns = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df[data_columns].resample('MS').mean()
df_monthly_mean.head()




warnings.filterwarnings("ignore")
plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Temperature and Humidity with time")
sns.lineplot(data=df_monthly_mean)

df1 = df_monthly_mean[df_monthly_mean.index.month==4]
print(df1)
df1.dtypes

import matplotlib.dates as mdates
fig, ax = plt.subplots(figsize=(18,7))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %Y'))
ax.legend(loc ='center right')
ax.set_xlabel('Month of April')

sns.lmplot(x='Apparent Temperature (C)',y='Humidity',data=df_monthly_mean)
plt.show()

corr = df_monthly_mean.corr()
sns.heatmap(corr)

sns.distplot(df.Humidity,color='red')

sns.relplot(data=df,x="Apparent Temperature (C)", y="Humidity", color="purple", hue="Summary")

plt.figure(figsize = (14 , 5))
sns.barplot(x = 'Apparent Temperature (C)', y = 'Humidity', data = np.round(df1, decimals=2))

