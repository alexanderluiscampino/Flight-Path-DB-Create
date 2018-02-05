# Flight-Path-DB-Create
This script takes as an Input .csv file where each row has information about a certain connection between two points. This can be a flight, a drive, bike riding, etc. In order to have Tableau producing a map where connecting points are shows, the format of the data needs to be different. This is achieved by this small script.

# Input CSV file:
**YEAR**|**MONTH**|**DAY OF WEEK**|**FL DATE**|**AIRLINE ID**|**CARRIER**|**FL NUM**|**ORIGIN**|**ORIGIN CITY\_NAME**|**DEST**|**DEST CITY\_NAME**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|19805|AA|1|JFK|New York, NY|LAX|Los Angeles, CA


# Ouput CSV file
**year**|**month**|**day of week**|**date**|**Carrier**|**fl number**|**path id**|**airport**|**city**|**path order**|**distance**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|AA|1|JFK\_LAX|JFK|New York, NY|1|2475
2016|4|5|4/1/2016|AA|1|JFK\_LAX|LAX|Los Angeles, CA|2|2475

# Usage
Simply add the .csv files to the folder named "No Path DB". If the file headers match the ones above, the routine can be run immediately. If that is not the case, the file fieldNames.py needs to be changed to match the dataset given. 

Follow the instructions [here](https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_howto_origin_destination.html) to create maps such as [this](https://public.tableau.com/en-us/s/blog/2015/05/visualizing-more-five-million-flights)
