import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./bases/suicide/master_ajustado.csv")
df = df[(df["country"]=="Brazil") & (df["year"]==2015)].groupby(["age", "year"]).sum()
df = df.reset_index(level=['age', 'year'])

suicides=[]
map(lambda (i,r): suicides.append(int(r)) ,enumerate(df["suicides"]))

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '5-14 anos(%d)'%suicides[3],'15-24 anos(%d)'%suicides[0], '25-34 anos(%d)'%suicides[1], '35-54 anos(%d)'%suicides[2], '55-74 anos(%d)'%suicides[4], '75+ anos(%d)'%suicides[5]
sizes = [suicides[3], suicides[0], suicides[1], suicides[2], suicides[4], suicides[5]]

sizes = map(lambda x: x*100.0/sum(suicides),sizes)

explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.set(title='Taxa de suicidios no Brasil, 2015 - Total:%d\n'%(sum(suicides)))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# # ###########################################################################

df = pd.read_csv("./bases/suicide/master_ajustado.csv")
df = df[(df["year"]==2015)].groupby(["age", "year"]).sum()
df = df.reset_index(level=['age', 'year'])
suicides=[]
map(lambda (i,r): suicides.append(int(r)) , enumerate(df["suicides"]))

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '5-14 anos(%d)'%suicides[3],'15-24 anos(%d)'%suicides[0], '25-34 anos(%d)'%suicides[1], '35-54 anos(%d)'%suicides[2], '55-74 anos(%d)'%suicides[4], '75+ anos(%d)'%suicides[5]
sizes = [suicides[3], suicides[0], suicides[1], suicides[2], suicides[4], suicides[5]]

sizes = map(lambda x: x*100.0/sum(suicides),sizes)

explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.set(title='Taxa de suicidios no mundo, 2015 - Total:%d\n'%(sum(suicides)))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()