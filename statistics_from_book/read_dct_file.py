import pandas as pd
from statadict import parse_stata_dict
import time
import numpy as np
import pickle
from collections import defaultdict

start_time = time.perf_counter()

try:
    with open('selected_variables_data.pickle', 'rb') as read_file:
        selected_variables_data = pickle.load(read_file)
except:

    stata_dict = parse_stata_dict(file="2002FemPreg.dct")
    data = pd.read_fwf("2002FemPreg.dat", names=stata_dict.names, colspecs=stata_dict.colspecs)



    ##### Selecting only required columns from 243 available columns
    # caseid is the integer ID of the respondent
    # prglength is the integer duration of pregnancy in weeks
    # outcome is an integer code for the outcome of pregnancy. Code 1 indicates a live birth
    # pregordr is pregnancy serial number; for first pregnancy it is 1, and second pregnancy is 2 and so on
    # birthord is serial number for live births; code for first child is 1, and so on. For outcomes other than live birth, this field is blank
    # birthwgt_lb and birthwgt_oz contains the pounds and ounces parts of the birth weight of the baby
    # agepreg is the mother's age at the end of pregnancy
    # finalwgt is the statistical weight assosciated with the respondent. It is the floating point value that indicates the number of people in US population this respondent represents.


    # selected_variables_data = data[['caseid', 'prglength', 'outcome', 'pregordr',
    #                                 'birthord', 'birthwgt_lb', 'birthwgt_oz',
    #                                 'agepreg', 'finalwgt']]

    data['prglength'] = (data.apply(lambda x:x['wksgest'] if x['wksgest'] else x['mosgest']*4.33, axis=1))

    selected_variables_data = data[['caseid', 'prglength', 'outcome', 'pregordr',
                                    'birthord', 'birthwgt_lb', 'birthwgt_oz',
                                    'agepreg', 'finalwgt']]

    with open('selected_variables_data.pickle', 'wb') as file:
        pickle.dump(obj=selected_variables_data, file=file)



##### DATA CLEANING
# since agepreg is encoded as an integer number of centiyears, hence devide age by 100

def data_cleaning():
    selected_variables_data['agepreg'] = selected_variables_data['agepreg'].apply(lambda x: x / 100)
    na_vals = [97, 98, 99]
    selected_variables_data.loc[selected_variables_data['birthwgt_lb'] > 20, 'birthwgt_lb'] = np.nan
    selected_variables_data['birthwgt_lb'] = selected_variables_data['birthwgt_lb'].apply(lambda x:x if x not in na_vals else np.nan)
    selected_variables_data['birthwgt_oz'] = selected_variables_data['birthwgt_oz'].apply(lambda x:x if x not in na_vals else np.nan)
    selected_variables_data['totalwgt_lb'] = (selected_variables_data['birthwgt_lb'] + selected_variables_data[
        'birthwgt_oz']) / 16.0
    return selected_variables_data

cleaned_data = data_cleaning().copy()




##### DATA VALIDATION

# # value counts will give in the descending order
# print(cleaned_data['outcome'].value_counts())
#
# # value counts with sort_values will give results in ascending order
# print(cleaned_data['outcome'].value_counts().sort_values())
#
# # check out for the birthweight
# print(cleaned_data['birthwgt_lb'].value_counts())
# From the above we observe that one baby has weighted in at 51 pounds, which is quite huge


##### DATA INTERPRETATION

e = defaultdict(list)
print({e[caseid].append(index) for index, caseid in cleaned_data['caseid'].iteritems()})
print(e)

# look at an example caseid
caseid = 10229
indices_caseid = e[caseid]
print(cleaned_data.loc[indices_caseid])

#         caseid  prglength  outcome  ...  agepreg     finalwgt  totalwgt_lb
# 11093   10229        2.0        4  ...    19.58  3369.662656          NaN
# 11094   10229        3.0        4  ...    21.75  3369.662656          NaN
# 11095   10229        4.0        4  ...    23.83  3369.662656          NaN
# 11096   10229        2.0        4  ...    25.50  3369.662656          NaN
# 11097   10229        3.0        4  ...    29.08  3369.662656          NaN
# 11098   10229       13.0        4  ...    32.16  3369.662656          NaN
# 11099   10229       43.0        1  ...    33.16  3369.662656        1.125
#

# Above result shows that caseid = 10229 had seven pregnancies and first six were miscarriages, and seventh one was successful

end_time = time.perf_counter()
total_time = end_time - start_time
print(f'Total time: {total_time}')








