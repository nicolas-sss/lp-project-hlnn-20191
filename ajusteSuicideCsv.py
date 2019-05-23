import csv
import numpy as np

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
            def map_content(r):
                if(pais[0] != r[0] or ano[0] != r[1]):
                    if(soma_populacao[0] != 0):
                        novo_csv.writerow([pais[0],ano[0],soma_suicidio[0],soma_populacao[0],((soma_suicidio[0]*100000)/soma_populacao[0])])
                    else:
                        novo_csv.writerow([pais[0],ano[0],soma_suicidio[0],soma_populacao[0],0])
                    pais[0] = r[0]
                    ano[0] = r[1]
                    soma_suicidio[0] = 0
                    soma_populacao[0] = 0
                soma_suicidio[0] += int(r[4])
                soma_populacao[0] += int(r[5])
            map(map_content,iterrdr)
            novo_csv.writerow(['null',0,0,0,0])

def runfiltro():
    row_suicide = ['country','year','suicides','population','suicides100']
    with open("./bases/suicide/master_pool.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/suicide/master_filtrado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_suicide)
            iterrdr = iter(rdr)
            next(iterrdr)
            pais = ['spoiler_avengers']
            ano = [0]
            lista_row = []
            def map_content(r, lista_row):
                if(int(r[1]) < 2000 or int(r[1]) > 2015):
                    return
                if(ano[0] != (r[1])):  
                    ano[0] = int(r[1])
                if(pais[0] != r[0]):
                    if(len(lista_row) > 10):
                        map(novo_csv.writerow,lista_row)
                    pais[0] = r[0]
                    del lista_row[:]
                lista_row.append(r)
            map(lambda r: map_content(r, lista_row),iterrdr)
            novo_csv.writerow(['null',0,0,0,0])

def runAjuste2():
    row_suicide = ['country','year','suicides','population','suicides100']
    with open("./bases/suicide/master_filtrado.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/suicide/master_ajustado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_suicide)
            iterrdr = iter(rdr)
            next(iterrdr)
            pais = ['spoiler_avengers']
            ano = [999999999]
            lista_row = []
            def map_content(r, lista_row):
                if(ano[0] != int(r[1])):
                    if int(r[1]) != (ano[0] + 1) and int(r[1]) > ano[0]:
                        map(lambda x:lista_row.append([r[0],(ano[0]+x),np.nan,np.nan,'null']),range(1,int(r[1])-ano[0]))
                    ano[0] = int(r[1])
                if(pais[0] != r[0]):
                    if(len(lista_row) < 16):
                        map(lambda x:lista_row.append([pais[0],2015-x,np.nan,np.nan,'null']),range(15-len(lista_row),-1,-1))
                    map(novo_csv.writerow,lista_row)
                    pais[0] = r[0]
                    del lista_row[:]
                lista_row.append(r)
            map(lambda r: map_content(r, lista_row), iterrdr)
runAjuste()
runfiltro()
runAjuste2()