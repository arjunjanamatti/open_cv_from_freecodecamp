import pandas as pd
from statadict import parse_stata_dict
import time
import numpy as np
import pickle



try:
    with open('cleaned_data.pickle', 'rb') as read_file:
        selected_variables_data = pickle.load(read_file)
except:

    start_time = time.perf_counter()
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

    print(selected_variables_data.info())

    print()

    ##### DATA CLEANING
    # since agepreg is encoded as an integer number of centiyears, hence devide age by 100

    def data_cleaning():
        selected_variables_data['agepreg'] = selected_variables_data['agepreg'].apply(lambda x: x / 100)
        na_vals = [97, 98, 99]
        selected_variables_data['birthwgt_lb'] = selected_variables_data['birthwgt_lb'].apply(lambda x:x if x not in na_vals else np.nan)
        selected_variables_data['birthwgt_oz'] = selected_variables_data['birthwgt_oz'].apply(lambda x:x if x not in na_vals else np.nan)
        selected_variables_data['totalwgt_lb'] = (selected_variables_data['birthwgt_lb'] + selected_variables_data[
            'birthwgt_oz']) / 16.0
        return selected_variables_data

    selected_variables_data = data_cleaning()

    with open('cleaned_data.pickle', 'wb') as file:
        pickle.dump(obj=selected_variables_data, file=file)


##### DATA VALIDATION

print(selected_variables_data)

end_time = time.perf_counter()
total_time = end_time - start_time
print(f'Total time: {total_time}')








