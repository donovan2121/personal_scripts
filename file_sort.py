import shutil, os, time
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG, format ='%(asctime)s - %(levelname)s - %(message)s')

# set default path to Path.cwd()
# will need to place this script 

#dict to map year: [month]
date_map = {}
file_date= []

def create_date(file_name):
    #get Modify time for each file 
    ti_m = os.path.getmtime(file_name)

    #convert float value time to string
    m_ts = time.ctime(ti_m)


    file_date = m_ts.split()

    file_year, file_month, file_day, file_time = file_date[-1], file_date[1], file_date[2], file_date[3]

    date_map.setdefault(file_year, [file_month])

    # append new date to list
    if file_month not in date_map[file_year]:
        date_map[file_year] += [file_month]
    

#loop for each file in folder:

# for file_name in os.listdir('./testmkdir/'):
#     path = Path.cwd() / 'testmkdir/' / file_name
#     create_date(path)
#     logging.debug(f'{file_name} mapped to dictionary.')

# print(date_map)





# test

file1 = {
    'year': '2022',
    'month': 'Jun'
}

file2 = {
    'year': '2020',
    'month': 'Apr'
}

file_date.append(file1)
file_date.append(file2)

for f in file_date:
    print(f['year'])

