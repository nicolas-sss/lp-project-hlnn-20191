import csv

def runAjuste():
    row_suicide = ['country','year','suicides','population','suicides100']
    with open("./bases/suicide/master.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/suicide/master_pool.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_suicide)
            iterrdr = iter(rdr)
            next(iterrdr)
            pais = ['spoiler_avengers']
            ano = [0]
            soma_suicidio = [0]
            soma_populacao = [0]
            def map_content(row):
                if(pais[0] != row[0] or ano[0] != row[1]):
                    if(soma_populacao[0] != 0):
                        novo_csv.writerow([pais[0],ano[0],soma_suicidio[0],soma_populacao[0],((soma_suicidio[0]*100000)/soma_populacao[0])])
                    else:
                        novo_csv.writerow([pais[0],ano[0],soma_suicidio[0],soma_populacao[0],0])
                    pais[0] = row[0]
                    ano[0] = row[1]
                    soma_suicidio[0] = 0
                    soma_populacao[0] = 0
                soma_suicidio[0] += int(row[4])
                soma_populacao[0] += int(row[5])
            map(map_content,iterrdr)

def runfiltro():
    row_suicide = ['country','year','suicides','population','suicides100']
    with open("./bases/suicide/master_pool.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/suicide/master_filtrado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_suicide)
            iterrdr = iter(rdr)
            next(iterrdr)
            lista_row = []
            pais = ['spoiler_avengers']
            ano = [0]
            def map_content(row):
                global lista_row
                if(ano[0] != (row[1])):
                    ano[0] = int(row[1])
                if(pais[0] != row[0]):
                    pais[0] = row[0]
                    lista_row = []
                if(ano[0] < 1990 or ano[0] > 2015):
                    return
                lista_row.append(row)
                if(len(lista_row) == 26):
                    map(novo_csv.writerow,lista_row)
            map(map_content,iterrdr)
                
runAjuste()
runfiltro()