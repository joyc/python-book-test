#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/9/19 22:35
# @Author  : Hython.com
# @File    : csvtest.py - Removes header from all CSV files.
import csv, os

os.makedirs('new_csv', exist_ok=True)

# Loop through
for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue
    print('Removing header from ' + csv_filename + '...')

csv_rows = []
csv_file = open(csv_filename)
reader = csv.reader(csv_file)
for row in reader:
    if reader.line_num == 1:
        continue
    csv_rows.append(row)
csv_file.close()

# add ";" to first col
print(csv_rows)

# write to new csv file
# csv_file = open(os.path.join('new_csv', csv_filename), 'w',
#                 newline='')
# csv_writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
# for row in csv_rows:
#     csv_writer.writerow(row)
# csv_file.close()
