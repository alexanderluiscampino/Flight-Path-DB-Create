# Fieldnames will be column headers on the output .csv file. Change as needed.
def fieldnames():
    return ['year', 'month', 'day_of_week', 'date', 'carrier',
                'fl_number', 'path_id', 'airport', 'city', 'path_order',
                 'distance', 'diverted', 'cancelled', 'cancel_code', 'arr_delay',
                  'dep_delay', 'taxi_out', 'taxi_in', 'carrier_delay',
                   'weather_delay', 'NAS_delay', 'sec_delay', 'late_delay']

# Function to create the output .csv column entries. These entries are the
# ones different on both line of the path
# Change it accordingly on the right hand side to the entries on the file of
# origin
# if path has more points besides origin and destination, these can be added
# bellow as a 3rd field, and changing the fieldame path-order to 3 and adding
# on commonEntries a different path_id, which is unique.
def dict_path(line,option):
    return {
        'origin': {fieldnames()[7]: line['ORIGIN'],
                    fieldnames()[8]: line['ORIGIN_CITY_NAME'],
                    fieldnames()[9]: 1},

        'destination': {fieldnames()[7]: line['DEST'],
                        fieldnames()[8]: line['DEST_CITY_NAME'],
                        fieldnames()[9]: 2},

    }[option]

# Function to create common dict entries. Both path rows will contain same info
# If needed change fields on righthand side to match input csv file
# Change formula applied on each field

def commonEntries(line):
    return {
            fieldnames()[0]: int(line['YEAR']),
            fieldnames()[1]: int(line['MONTH']),
            fieldnames()[2]: int(line['DAY_OF_WEEK']),
            fieldnames()[3]: line['FL_DATE'],
            fieldnames()[4]: line['CARRIER'],
            fieldnames()[5]: line['FL_NUM'],
            fieldnames()[6]: line['ORIGIN'] + '_' + line['DEST'],
            fieldnames()[10]: int(line['DISTANCE'].split('.')[0]),
            fieldnames()[11]: int(line['DIVERTED'].split('.')[0]) if line['DIVERTED'] != '' else 0,
            fieldnames()[12]: int(line['CANCELLED'].split('.')[0]) if line['CANCELLED'] != '' else 0,
            fieldnames()[13]: line['CANCELLATION_CODE'] if line['CANCELLATION_CODE'] != '' else 'NC',
            fieldnames()[14]: int(line['ARR_DELAY'].split('.')[0]) if line['ARR_DELAY'] != '' else 0,
            fieldnames()[15]: int(line['DEP_DELAY'].split('.')[0]) if line['DEP_DELAY'] != '' else 0,
            fieldnames()[16]: int(line['TAXI_OUT'].split('.')[0]) if line['TAXI_OUT'] != '' else 0,
            fieldnames()[17]: int(line['TAXI_IN'].split('.')[0]) if line['TAXI_IN'] != '' else 0,
            fieldnames()[18]: int(line['CARRIER_DELAY'].split('.')[0]) if line['CARRIER_DELAY'] != '' else 0,
            fieldnames()[19]: int(line['WEATHER_DELAY'].split('.')[0]) if line['WEATHER_DELAY'] != '' else 0,
            fieldnames()[20]: int(line['NAS_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
            fieldnames()[21]: int(line['SECURITY_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0,
            fieldnames()[22]: int(line['LATE_AIRCRAFT_DELAY'].split('.')[0]) if line['NAS_DELAY'] != '' else 0
            }
