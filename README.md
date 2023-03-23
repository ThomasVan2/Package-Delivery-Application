# Package-Delivery-Application

## Introduction ## 
This is a project to address a package delivery routing issue, which is similar to the traveling salesman problem but with certain limitations and prerequisites. To tackle this problem, I utilized the nearest neighbor algorithm, which has a time complexity of O(n).


### Description ###
This program is written in Python and solves the vehicle routing problem for a package delivery service. It reads three CSV files containing package information, distance between locations, and another distance matrix, which it uses to create package, distance, and truck objects. The code also defines functions for loading the package information, getting the distance from a matrix list, getting the address ID from a package, finding the closest address, converting decimal numbers to time,  and converting time to a decimal number. The program then uses the nearest neighbour alogarithm to find the optimal route for each truck. The command line interface is used for insert and look-up functions to view the status of any package at any time and gives the option to display the routes on a map using the Folium library. The output is a visual representation of the truck's route and the addresses of the packages on that route.


#### Assumptions: ####

* Each truck has a capacity to carry a maximum of 16 packages.
* The trucks maintain an average speed of 18 miles per hour during their journey.
* The trucks do not require any refueling during their journey as they have an infinite amount of gas.
* Each driver is assigned to a specific truck for the entire day.
* The drivers start their journey at 8:00 a.m. with the truck fully loaded, and they can return to the hub to collect more packages if necessary. The day ends when all 40 packages are delivered.
* The delivery time is considered to be instantaneous, so the time taken to deliver a package is already factored into the average speed of the trucks.
* There may be a special note associated with a package, but there is a maximum of one note per package.
* The incorrect delivery address for package #9, Third District Juvenile Court, will be rectified at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
* Each package has a unique ID, and there will be no duplication of IDs.
* No additional assumptions are allowed or required.
