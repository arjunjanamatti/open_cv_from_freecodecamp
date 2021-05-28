import pandas as pd
from statadict import parse_stata_dict

stata_dict = parse_stata_dict(file="2002FemPreg.dct")
data = pd.read_fwf("2002FemPreg.dat", names=stata_dict.names, colspecs=stata_dict.colspecs)

print(data.head())
print()
print(f'Shape of the dataframe: {data.shape}')
print(data.columns)






