import pandas as pd
from statadict import parse_stata_dict
import time

start_time = time.perf_counter()
stata_dict = parse_stata_dict(file="2002FemPreg.dct")
data = pd.read_fwf("2002FemPreg.dat", names=stata_dict.names, colspecs=stata_dict.colspecs)

end_time = time.perf_counter()
total_time = end_time - start_time
print(f'Total time: {total_time}')
print()
print(data.head())
print()
print(f'Shape of the dataframe: {data.shape}')
print(len(data.columns))








