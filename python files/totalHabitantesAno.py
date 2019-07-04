# import csv
import numpy as np;
import pandas as pd;

dfPopulation=pd.read_csv("./bases/wdi/country_population.csv")
keep_col = ['country','year','population']
dfPopulationFixed = pd.melt(dfPopulation, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                var_name='year', value_name='population')
dfPopulationFixed.columns.values[0] = 'country'
dfPopulationFixed['year'] = dfPopulationFixed['year'].astype(int)
dfPopulationFixed = dfPopulationFixed[keep_col].sort_values(by=['country', 'year'])
dfPopulationFixed = dfPopulationFixed[(dfPopulationFixed['year'] >= 2000) & (dfPopulationFixed['year'].astype(int) <= 2015)]

dfMaster = pd.read_csv("./bases/suicide/master_ajustado.csv")
pais = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Ecuador', 'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Mauritius', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Panama', 'Paraguay', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saint Lucia', 'Saint Vincent and Grenadines', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Suriname', 'Sweden', 'Switzerland', 'Thailand', 'Trinidad and Tobago', 'Turkmenistan', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay']
dfMaster = dfMaster[(dfMaster['country'] != 'spoiler_avengers') & (dfMaster['country'].isin(pais))].reset_index(drop=True)
# print(dfMaster)
del dfMaster['population']
dfMaster = pd.merge(dfPopulationFixed, dfMaster, on=['country','year'])
dfMaster = dfMaster.pivot_table(['population','suicides','suicides100'], ['country', 'year'])
dfMaster = dfMaster.interpolate(method='pad', limit_direction='both', axis=1).reset_index(level=['country', 'year'])
dfMaster['suicides100'] = dfMaster.apply(lambda row: int(row['suicides'])*100000/row['population'] if not np.isnan(row['suicides']) else np.nan,axis=1)
print(dfMaster)
dfMaster.to_csv("./bases/suicide/master_correcao.csv",index=False)


# new_f.to_csv("./bases/wdi/Country_ajustado.csv", index=False)

# def runPopulation():
#     row_population = ['country','year','population']
#     with open("./bases/wdi/country_population.csv","rb") as source:
#         rdr= csv.reader( source )
#         with open("./bases/suicide/country_population.csv","wb") as result:
#             novo_csv = csv.writer( result )
#             novo_csv.writerow(row_population)
#             iterrdr = iter(rdr)
#             next(iterrdr)
#             lista_row=[]
#             def map_content(row):
#                 #pais,ano,populacao
#                 map(lambda x: lista_row.append([row[0], 2000+x,row[x+44]]), range(0,16))
#                 if len(lista_row)/16 == 264:
#                     map(novo_csv.writerow, lista_row)
#             map(map_content,iterrdr)

# def mergeMasterPopulation():
#     row_suicide = ['country','year','suicides','population','suicides100']
#     with open("./bases/suicide/master_ajustado.csv","rb") as source:
#         master= csv.reader( source )
#         with open("./bases/suicide/country_populationFix.csv", "rb") as otherSource:
#             popul= csv.reader( otherSource )
#             with open("./bases/suicide/master_correcao.csv","wb") as result:
#                 novo_csv = csv.writer( result )
#                 novo_csv.writerow(row_suicide)
#                 itermaster = iter(master)
#                 iterpopul = iter(popul)
#                 next(itermaster)
#                 next(iterpopul)
#                 iterpopul=list(iterpopul)
                
#                 pais = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Ecuador', 'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Mauritius', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Panama', 'Paraguay', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saint Lucia', 'Saint Vincent and Grenadines', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Suriname', 'Sweden', 'Switzerland', 'Thailand', 'Trinidad and Tobago', 'Turkmenistan', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay']
#                 lista_row = []
#                 def map_iterpopul(masterRow, populRow):
#                     if (masterRow[0] == populRow[0]) and (masterRow[1] == populRow[1]):
#                         if masterRow[0] in pais:
#                             if(masterRow[2] == 'nan'):
#                                 lista_row.append([masterRow[0], masterRow[1], masterRow[2], populRow[2], 'null'])
#                             else:
#                                 popPer100=(float(int(masterRow[2])*100000)/float(populRow[2]))
#                                 lista_row.append([masterRow[0], masterRow[1], masterRow[2], populRow[2], popPer100])
#                 def map_itermaster(row):
#                     map(lambda x: map_iterpopul(row,x), iterpopul)
#                 map(map_itermaster,itermaster)
#                 print(len(reduce(lambda l, x: l.append(x[0]) or l if x[0] not in l else l, lista_row, [])))
#                 map(novo_csv.writerow,lista_row)

# runPopulation()
# adjustCountry()
# mergeMasterPopulation()
