import csv
import os
import xlrd
import time
import sys
###############################################################################
def create_dict_line(line,option):
    return {
        'origin': {'year': int(line['YEAR']),
                        'month': int(line['MONTH']),
                        'day_of_week': int(line['DAY_OF_WEEK']),
                        'date': line['FL_DATE'],
                        'Carrier': line['CARRIER'],
                        'fl_number': line['FL_NUM'],
                        'path_id': line['ORIGIN'] + '_' + line['DEST'],
                        'airport': line['ORIGIN'],
                        'city': line['ORIGIN_CITY_NAME'],
                        'path_order': 1,
                        'distance': int(line['DISTANCE'].split('.')[0]),
                        'diverted': int(line['DIVERTED'].split('.')[0]) if line['DIVERTED'] != '' else 0,
                        'cancelled': int(line['CANCELLED'].split('.')[0]) if line['CANCELLED'] != '' else 0,
                        'cancel_code': line['CANCELLATION_CODE'] if line['CANCELLATION_CODE'] != '' else 'NC',
                        'arr_delay': int(line['ARR_DELAY'].split('.')[0]) if line['ARR_DELAY'] != '' else 0,
                        'dep_delay': int(line['DEP_DELAY'].split('.')[0]) if line['DEP_DELAY'] != '' else 0,
                        'taxi_out': int(line['TAXI_OUT'].split('.')[0]) if line['TAXI_OUT'] != '' else 0,
                        'taxi_in': int(line['TAXI_IN'].split('.')[0]) if line['TAXI_IN'] != '' else 0,
                        'carrier_delay': int(line['CARRIER_DELAY'].split('.')[0]) if line['CARRIER_DELAY'] != '' else 0,
                        'weather_delay': int(line['WEATHER_DELAY'].split('.')[0]) if line['WEATHER_DELAY'] != '' else 0,
                        'NAS_delay': int(line['NAS_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
                        'sec_delay': int(line['SECURITY_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
                        'late_delay': int(line['LATE_AIRCRAFT_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0},

        'destination': {'year': int(line['YEAR']),
                        'month': int(line['MONTH']),
                        'day_of_week': int(line['DAY_OF_WEEK']),
                        'date': line['FL_DATE'],
                        'Carrier': line['CARRIER'],
                        'fl_number': line['FL_NUM'],
                        'path_id': line['ORIGIN'] + '_' + line['DEST'],
                        'airport': line['DEST'],
                        'city': line['DEST_CITY_NAME'],
                        'path_order': 2,
                        'distance': int(line['DISTANCE'].split('.')[0]),
                        'diverted': int(line['DIVERTED'].split('.')[0]) if line['DIVERTED'] != '' else 0,
                        'cancelled': int(line['CANCELLED'].split('.')[0]) if line['CANCELLED'] != '' else 0,
                        'cancel_code': line['CANCELLATION_CODE'] if line['CANCELLATION_CODE'] != '' else 'NC',
                        'arr_delay': int(line['ARR_DELAY'].split('.')[0]) if line['ARR_DELAY'] != '' else 0,
                        'dep_delay': int(line['DEP_DELAY'].split('.')[0]) if line['DEP_DELAY'] != '' else 0,
                        'taxi_out': int(line['TAXI_OUT'].split('.')[0]) if line['TAXI_OUT'] != '' else 0,
                        'taxi_in': int(line['TAXI_IN'].split('.')[0]) if line['TAXI_IN'] != '' else 0,
                        'carrier_delay': int(line['CARRIER_DELAY'].split('.')[0]) if line['CARRIER_DELAY'] != '' else 0,
                        'weather_delay': int(line['WEATHER_DELAY'].split('.')[0]) if line['WEATHER_DELAY'] != '' else 0,
                        'NAS_delay': int(line['NAS_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
                        'sec_delay': int(line['SECURITY_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
                        'late_delay': int(line['LATE_AIRCRAFT_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0},

    }[option]
###############################################################################
def fieldnames():
    return ['year', 'month', 'day_of_week', 'date', 'Carrier',
                'fl_number', 'path_id', 'airport', 'city', 'path_order',
                 'distance', 'diverted', 'cancelled', 'cancel_code', 'arr_delay',
                  'dep_delay', 'taxi_out', 'taxi_in', 'carrier_delay',
                   'weather_delay', 'NAS_delay', 'sec_delay', 'late_delay']
###############################################################################
cwd = os.getcwd()
csvDir = os.listdir(cwd + "/No Path DB")
output_file = 'path_db.csv'
with open(os.path.join('Path DB',output_file), 'w+') as outputcsv:
    writer = csv.DictWriter(outputcsv, delimiter=',', lineterminator='\n',fieldnames=fieldnames())
    writer.writeheader()
    for file_ in csvDir:
        if file_.endswith(".csv"):
            with open(os.path.join('No Path DB',file_)) as csv_file:
                reader = csv.DictReader(csv_file)
                for line in reader:
                    writer.writerow(create_dict_line(line,'origin'))
                    writer.writerow(create_dict_line(line,'destination'))
