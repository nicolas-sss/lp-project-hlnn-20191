import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import csv    
# import numpy as np

df = pd.io.parsers.read_csv("./bases/wdi/temp/indicators_ajustado.csv")

filtro1 = (df['indicator'] == 'SP.DYN.LE00.IN')
filtro2 =  (df['indicator'] == 'SP.DYN.LE00.FE.IN')
filtro3 = (df['indicator'] == 'SP.DYN.LE00.MA.IN')

grouped = df.where(filtro1 | filtro2 | filtro3 ).dropna()
grouped = grouped.groupby(['year','indicator']).agg({'value':'mean'})
grouped = grouped.reset_index(level=['year', 'indicator'])
print grouped

#plt2 = plt.plot( 'year', 'population', data=grouped, marker='', color='olive', linewidth=2)
fig, ax = plt.subplots()
ax.set_title("Expectativa de vida")
ax.set_xlabel("Ano")
ax.set_ylabel("Anos de vida")
plt.grid(axis='y', linestyle='-')
plt.xticks(range(1990,2014))


plt.plot( 'year', 'value', data=grouped.where(grouped['indicator'] == 'SP.DYN.LE00.IN').dropna(), marker='o', markerfacecolor='olive', color='y', linewidth=2, markersize=4)
plt.plot( 'year', 'value',  linestyle='-', data=grouped.where(grouped['indicator'] == 'SP.DYN.LE00.MA.IN').dropna(), marker='o', color='skyblue', linewidth=2, markerfacecolor='blue', markersize=4)
plt.plot( 'year', 'value',  linestyle='-', data=grouped.where(grouped['indicator'] == 'SP.DYN.LE00.FE.IN').dropna(), marker='o', color='lightcoral', linewidth=2, markerfacecolor='indianred', markersize=4)
plt.legend()
plt.show()
