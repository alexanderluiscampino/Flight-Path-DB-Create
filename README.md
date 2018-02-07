# Flight-Path-DB-Create
This script takes as an Input .csv file where each row has information about a certain connection between two points. This can be a flight, a drive, bike riding, etc. In order to have Tableau producing a map where connecting points are shows, the format of the data needs to be different. This is achieved by this small script.
_______________________________________________________________________________________________________________________________________

# Installation
Simply fork this project to your repository. Access the fileEntries.py to change the fieldnames to ones of your choice. Also change the columns names to match the ones in the input .csv file.

## Version
Written using *Python 3* with all libraries installed from the package Anaconda. If any package/library is missing, use the command line:
  - pip install missingPackage

# Usage
Simply add the .csv files to the folder named "No Path DB". If the file headers match the ones above, the routine can be run immediately. If that is not the case, the file fieldNames.py needs to be changed to match the dataset given. 


### Input CSV file:
**YEAR**|**MONTH**|**DAY OF WEEK**|**FL DATE**|**AIRLINE ID**|**CARRIER**|**FL NUM**|**ORIGIN**|**ORIGIN CITY\_NAME**|**DEST**|**DEST CITY\_NAME**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|19805|AA|1|JFK|New York, NY|LAX|Los Angeles, CA


### Ouput CSV file
**year**|**month**|**day of week**|**date**|**Carrier**|**fl number**|**path id**|**airport**|**city**|**path order**|**distance**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
2016|4|5|4/1/2016|AA|1|JFK\_LAX|JFK|New York, NY|1|2475
2016|4|5|4/1/2016|AA|1|JFK\_LAX|LAX|Los Angeles, CA|2|2475

### Map Creation on Tableau
Follow the instructions [here](https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_howto_origin_destination.html) to create maps such as [this](https://public.tableau.com/en-us/s/blog/2015/05/visualizing-more-five-million-flights)

_______________________________________________________________________________________________________________________________________
## Built With

* [Atom Text Edit](https://atom.io/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Alexandre Campino** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Udacity Lessons
* Stack Overflow
* GitHub Repositories
