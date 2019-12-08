# Group68_mh3992_yw3410
 - Group 68, Section 2
 - UNIs: [mh3992, yw3410]
 - Here is the link to the server
 [here]

##Introduction
This is an application to track squirrels in the central park. Users can view squirrels' location on map, update, add and view general statistics on this web.

##Import and export data
Users can run command line to import and export data. The file path should be specified at the command line after the name of the management command. 

    #import data  
    $ python manage.py import_squirrel_data /path/to/file.csv  
    #export data  
    $ python manage.py export_squirrel_data /path/to/file.csv  

##Map
The nap displays the location of the squirrel sightings on an OpenStreets map.

##Sightings
The signtings page shows the data for all the squirrel sightings. On the top of this page, you can click on the buttons "add a new sighting" and "click to see the stats", which will direct you to the pages to add sightings and view general statistics. Also, you can click on the squirrels' id to update the data.  

