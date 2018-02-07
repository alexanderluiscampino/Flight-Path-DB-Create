import csv, os
from  lib.fileEntries import fieldnames, dict_path, commonEntries
###############################################################################
cwd = os.getcwd()
csvDir = os.listdir(cwd + "/No Path DB")
output_file = 'path_db.csv'
# Function to write lines on output csv file
with open(os.path.join('Path DB',output_file), 'w+') as outputcsv:
    writer = csv.DictWriter(outputcsv, delimiter=',', lineterminator='\n',fieldnames=fieldnames())
    writer.writeheader()
    for file_ in csvDir:
        if file_.endswith(".csv"):
            with open(os.path.join('No Path DB',file_)) as csv_file:
                reader = csv.DictReader(csv_file)
                for line in reader:
                    # Create dict with the entry to right to file
                    origin = dict_path(line,'origin')
                    origin.update(commonEntries(line)) # add common fields
                    destination = dict_path(line,'destination')
                    destination.update(commonEntries(line))
                    # Write to output file origin and destination*
                    writer.writerow(origin)
                    writer.writerow(destination)

#* if more than 2 points are needed, rearrange above to write an extra line on file
# for each path point. Use as many writer.writerow as there are points on path
# change fileEntries.py accordingly
