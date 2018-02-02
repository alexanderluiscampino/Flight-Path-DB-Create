# Flight-Path-DB-Create
This script takes as an Input .csv files. The csv files looks like the one bellow. It will output a new csv file with all entries combined in form of a path.


**YEAR**|**MONTH**|**DAY OF WEEK**|**FL DATE**|**AIRLINE ID**|**CARRIER**|**FL NUM**|**ORIGIN**|**ORIGIN CITY\_NAME**|**DEST**|**DEST CITY\_NAME**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|19805|AA|1|JFK|New York, NY|LAX|Los Angeles, CA



**year**|**month**|**day of week**|**date**|**Carrier**|**fl number**|**path id**|**airport**|**city**|**path order**|**distance**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|AA|1|JFK\_LAX|JFK|New York, NY|1|2475
2016|4|5|4/1/2016|AA|1|JFK\_LAX|LAX|Los Angeles, CA|2|2475
