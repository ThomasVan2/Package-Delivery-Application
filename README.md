# Package-Delivery-Application

## Introduction ## 
This is a project to address a package delivery routing issue, which is similar to the traveling salesman problem but with certain limitations and prerequisites. To tackle this problem, I utilized the nearest neighbor algorithm, which has a time complexity of O(n).


### Description ###
This program is written in Python and solves the vehicle routing problem for a package delivery service. It reads three CSV files containing package information, distance between locations, and another distance matrix, which it uses to create package, distance, and truck objects. The code also defines functions for loading the package information, getting the distance from a matrix list, getting the address ID from a package, finding the closest address, converting decimal numbers to time,  and converting time to a decimal number. The program then uses the nearest neighbour alogarithm to find the optimal route for each truck. The command line interface is used for insert and look-up functions to view the status of any package at any time and gives the option to display the routes on a map using the Folium library. The output is a visual representation of the truck's route and the addresses of the packages on that route.


#### Assumptions: ####

• Each truck can carry a maximum of 16 packages.

• Trucks travel at an average speed of 18 miles per hour.

• Trucks have a “infinite amount of gas” with no need to stop.

• Each driver stays with the same truck as long as that truck is in service.

• Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.

• Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).

• There is up to one special note for each package. • The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.

• The package ID is unique; there are no collisions.

• No further assumptions exist or are allowed."
