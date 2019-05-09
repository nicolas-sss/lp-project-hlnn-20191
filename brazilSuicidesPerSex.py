import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


df = pd.io.parsers.read_csv("./bases/suicide/master_ajustado.csv")
df = df[(df["country"]=="Brazil")].groupby(["year", "sex"]).sum()
df = df.reset_index(level=['year', 'sex'])

maleSuicides=[]
femaleSuicides=[]
for i, row in enumerate(df['suicides']):
        if i%2 == 0: #feminino 
              femaleSuicides.append(int(row)) 
        else: #masculino
                maleSuicides.append(int(row))

years = tuple(df['year'].unique())

#Masculino, Feminino

#Grafico

men_means = tuple(maleSuicides)
women_means = tuple(femaleSuicides)


ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width,
                color='SkyBlue', label='Men')
rects2 = ax.bar(ind + width/2, women_means, width,
                color='IndianRed', label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Taxa de suicidios ')
ax.set_title('Suicidios pelo ano e pelo genero')
ax.set_xticks(ind)
ax.set_xticklabels(years)
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()