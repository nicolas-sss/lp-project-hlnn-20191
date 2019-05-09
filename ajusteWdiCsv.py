import csv


def runAjuste():
    row_indicators = ['country','indicator','year','value']
    row_that_matter = ['SP.DYN.LE00.IN','SP.DYN.LE00.FE.IN','SP.DYN.LE00.MA.IN', 'BX.TRF.PWKR.CD.DT',
     'SP.POP.GROW', 'SP.POP.TOTL','SP.DYN.CBRT.IN','NY.GNP.MKTP.CD', 'IC.TAX.PAYM','FP.CPI.TOTL','SL.EMP.MPYR.ZS','GC.XPN.TOTL.CN','SL.TLF.PRIM.ZS']
    with open("./bases/wdi/Indicators.csv","r") as source:
        rdr = csv.reader(source, delimiter=',')
        parte = [0]
        novo_csv = [csv.writer(open('./bases/wdi/temp/indicators_ajustado.csv', 'w'), delimiter=',')]
        limite = [10000000]
        iterrdr = iter(rdr)
        next(iterrdr)
        novo_csv[0].writerow(row_indicators)
        def map_content(i,row):
            if int(row[4]) < 1990 or int(row[4]) > 2017:
                return
            if i + 1 > limite[0]:
                parte[0] += 1
                limite[0] = 10000000 * parte[0]
                novo_csv[0] = csv.writer(open('./bases/wdi/temp/indicators_%s.csv' % str(parte[0]), 'w'), delimiter=',')
                novo_csv[0].writerow(row_indicators)
            if (row[3] in row_that_matter):
                del row[2]
                del row[0]
                novo_csv[0].writerow(row)
        map(lambda (i,row): map_content(i, row) , enumerate(iterrdr))

def runFiltro():
    with open("./bases/wdi/indicators_ajustado.csv","r") as source:
        rdr = csv.reader(source, delimiter=',')


runAjuste()