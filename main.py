import csv
import os
import re

path = './census2011.csv'

if not os.path.exists(path):
    print('File does not exists')

with open(path, 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for col in reader:
        if not col[0].isnumeric():
            print('Invalid ID at row', reader.line_num)
        elif not re.match(r'^E1200000[1-9]$', col[1]) and col[1] != 'W92000004':
            print('Invalid region code at row', reader.line_num)
        elif col[2] is not 'H' or col[2] is not 'C':
            print('Invalid Residence Type code at row', reader.line_num)
        elif not re.match(r'^[1-6]$', col[3]) or col[3] != '-9':
            print('Invalid Family Composition code at row', reader.line_num)