import csv

def adjustCountry():
    paises = ['Kyrgyzstan', 'Uruguay', 'Saint Lucia', 'Bahamas', 'Republic of Korea', 'Saint Vincent and Grenadines', 'Slovakia']
    keep_col = ['CountryCode','ShortName','LongName','CurrencyUnit','Region']
    with open("./bases/wdi/Country_ajustado.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/wdi/Country_ajustadoFix.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(keep_col)
            iterrdr = iter(rdr)
            next(iterrdr)
            lista_row=[]
            def map_content(row):
                #pais,ano,populacao
                if(row[1] == 'Slovak Republic'):
                        novo_csv.writerow(([row[0], 'Slovakia', row[2],row[3],row[4]]))
                elif(row[1] == 'Kyrgyz Republic'):
                    novo_csv.writerow(([row[0], 'Kyrgyzstan', row[2],row[3],row[4]]))
                elif(row[1] == 'St. Lucia'):
                    novo_csv.writerow(([row[0], 'Saint Lucia', row[2],row[3],row[4]]))
                elif(row[1] == 'The Bahamas'):
                    novo_csv.writerow(([row[0], 'Bahamas', row[2],row[3],row[4]]))
                elif(row[1] == "Dem. People's Rep. Korea"):
                    novo_csv.writerow(([row[0], 'Republic of Korea', row[2],row[3],row[4]]))
                elif(row[1] == 'St. Vincent and the Grenadines'):
                    novo_csv.writerow(([row[0], 'Saint Vincent and Grenadines', row[2],row[3],row[4]]))
                elif(row[1] == 'Russia'):
                    novo_csv.writerow(([row[0], 'Russian Federation', row[2],row[3],row[4]]))
                else:
                    novo_csv.writerow(row)
            map(map_content,iterrdr)

def mergeMasterPopulation():
    row_suicide = ['country','year','suicides','population','suicides100']
    with open("./bases/wdi/Country_ajustadoFix.csv","rb") as source:
        master= csv.reader( source )
        with open("./bases/suicide/master_correcao.csv", "rb") as otherSource:
            popul= csv.reader( otherSource )
            with open("./bases/suicide/teste.csv","wb") as result:
                novo_csv = csv.writer( result )
                novo_csv.writerow(row_suicide)
                itermaster = iter(master)
                iterpopul = iter(popul)
                next(itermaster)
                next(iterpopul)
                iterpopul=list(iterpopul)
                
                pais = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Ecuador', 'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Mauritius', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Panama', 'Paraguay', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saint Lucia', 'Saint Vincent and Grenadines', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Suriname', 'Sweden', 'Switzerland', 'Thailand', 'Trinidad and Tobago', 'Turkmenistan', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay']
                lista_row = []
                paises = set([])
                def map_iterpopul(masterRow, populRow):
                    if(masterRow[1] in pais):
                        paises.add(masterRow[1])
                    if (masterRow[0] == populRow[0]) and (masterRow[1] == populRow[1]):
                        if masterRow[0] in pais:
                            if(masterRow[2] == 'nan'):
                                lista_row.append([masterRow[0], masterRow[1], masterRow[2], populRow[2], 'null'])    
                            else:
                                popPer100=(float(int(masterRow[2])*100000)/float(populRow[2]))
                                lista_row.append([masterRow[0], masterRow[1], masterRow[2], populRow[2], popPer100])
                def map_itermaster(row):
                    map(lambda x: map_iterpopul(row,x), iterpopul)
                map(map_itermaster,itermaster)
                print(len(reduce(lambda l, x: l.append(x[0]) or l if x[0] not in l else l, lista_row, [])))
                print(set(pais).difference(paises))
                map(novo_csv.writerow,lista_row)
adjustCountry()
mergeMasterPopulation()