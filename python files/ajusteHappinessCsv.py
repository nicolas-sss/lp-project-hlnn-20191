import csv

def runAjuste():
    row_happiness = ["country","hrank","hscore","economy","family","health","freedom","generosity","trust","dystopia"]

    with open("./bases/happiness/2015.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/happiness/2015_ajustado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_happiness)
            iterrdr = iter(rdr)
            next(iterrdr)
            def remove_unnecessary_cols(row):
                del row[4]
                del row[1]
                novo_csv.writerow(row)
            map(remove_unnecessary_cols,iterrdr)

    with open("./bases/happiness/2016.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/happiness/2016_ajustado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_happiness)
            iterrdr = iter(rdr)
            def remove_unnecessary_cols(row):
                del row[5]
                del row[4]
                del row[1]
                novo_csv.writerow(row)
            map(remove_unnecessary_cols,iterrdr)

    with open("./bases/happiness/2017.csv","rb") as source:
        rdr= csv.reader( source )
        with open("./bases/happiness/2017_ajustado.csv","wb") as result:
            novo_csv = csv.writer( result )
            novo_csv.writerow(row_happiness)
            iterrdr = iter(rdr)
            def remove_unnecessary_cols(row):
                del row[4]
                del row[3]
                novo_csv.writerow(row)
            map(remove_unnecessary_cols,iterrdr)

runAjuste()