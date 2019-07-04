import pandas as pd
f=pd.read_csv("./bases/wdi/Country.csv")
keep_col = ['CountryCode','ShortName','LongName','CurrencyUnit','Region']
new_f = f[keep_col]
new_f.to_csv("./bases/wdi/Country_ajustado.csv", index=False)