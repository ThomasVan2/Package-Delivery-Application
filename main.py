# Author: Thomas van Eekelen
# Student ID: 010433106
#1. Number the icons, make truck icon, make actual route
#optimize algo
import csv
import folium
import numpy as np
from geopy import location

from Truck import Truck
from HashMap import HashMap
from Package import Package

# Reading CVS files
with open("PackageCVS.csv") as PackageCVS:
    CSV_Package = csv.reader(PackageCVS)
    CSV_Package = list(CSV_Package)

with open("DistanceCVS.csv") as DistanceCVS:
    CVS_Distance = csv.reader(DistanceCVS)
    CVS_Distance = list(CVS_Distance)

with open("Distance2CVS.csv") as Distance2CVS:
    CVS2_Distance = csv.reader(Distance2CVS)
    CVS2_Distance = list(CVS2_Distance)

# Making package objects from the CVS file
# Loading the packages in the hash map
def loadPackageFile(fileName, myHash):
    with open(fileName) as packageCVS:
        packageData = csv.reader(packageCVS)
        next(packageData)
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = int(package[4])
            pDeadline = package[5]
            pWeight = int(package[6])
            pNotes = package[7]
            pLatitude = package[8]
            pLongitude = package[9]
            pStatus = "At the hub"
            pDelivery_time = 0
            pEnrouteTime = 0

            # Package Object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes, pStatus, pDelivery_time,
                        pEnrouteTime, pLatitude, pLongitude)

            myHash.add(pID, p)

myHash = HashMap()
loadPackageFile("PackageCVS.csv", myHash)

points1 = []
points2 = []
points3 = []

# Load the packages in the truck
listPackages1 = ['1', "2", "4", "13", "14", "15", "16", "17", "19", "20", "21", "22", "24", "33", "34", '40']
listPackages2 = ["3", "5", "8", "18", "26", "29", "30", "31", "36", "37", "38"]
listPackages3 = ["9", "10", "6", "7", "11", "12", "23", "25", "27", "28", "32", "35", "39"]

# 1.Make the lists with the prerequisite 2.Can use brute force logarithm to go through whole list/

# Creating Truck objects
truck1 = Truck(16, 18, 8, listPackages1, 0, len(listPackages1), 0, "At the hub", 0, points1)
truck2 = Truck(13, 18, 8, listPackages2, 0, len(listPackages2), 0, "At the hub", 0, points2)
truck3 = Truck(11, 18, None, listPackages3, 0, len(listPackages3), 0, "At the hub", 0, points3)

# Getting distance from matrix list by index
def getDistance(x, y):
    if x > y:
        return float(CVS2_Distance[x + 1][y])
    return float(CVS2_Distance[y][x + 1])

# Getting the address ID from the package
def getAddressId(address):
    for i, x in enumerate(CVS_Distance):
        if CVS_Distance[i][2].__contains__(address) or CVS_Distance[i][1].__contains__(address):
            return CVS_Distance[i]

# Gets the closest address
def closestAddress(x, packageList):
    minDistance = 100.50
    for i in range(len(packageList)):
        package = myHash.get(int(packageList[i]))
        addressId = getAddressId(package.address)
        distances = getDistance(x, int(addressId[0]))
        if distances < minDistance:
            minDistance = distances
            packageId = package.ID
            addressIdnew = addressId[0]
            latitude = package.pLatitude
            longitude = package.pLongitude
    return [minDistance, packageId, addressIdnew, latitude,longitude]

# Calculates decimal number to time
def decToTime(decimalTime):
    hours = int(decimalTime)
    minutes = (decimalTime * 60) % 60
    return "%d:%02d" % (hours, minutes)

# Formats input to HH:mm
def time_format(HH, mm):
    return "%d:%02d" % (HH, mm)

# Calculates time to decimal number
def timeToDec(time):
    try:
        fields = time.split(":")
        hours = fields[0] if len(fields) > 0 else 0.0
        minutes = fields[1] if len(fields) > 1 else 0.0
        if int(hours) > 24:
            print("Please enter valid time (HH:mm)\n")
            return False
        elif int(hours) == 24 and int(minutes) > 0:
            print("Please enter valid time (HH:mm)\n")
            return False
        else:
            return float(hours) + (float(minutes) / 60.0)
    except ValueError:
        print("Please enter valid time (HH:mm)\n")
        return False

map_delivery = folium.Map(location=[40.684853,  -111.870201], zoom_start=11, control_scale=True)

# Delivering trucks packages
def delivering(truck,marker):
    next_package_address = 0
    truck.mileage = 0
    i = 0
    truck.load = len(truck.listPackages)
    truck.status = "en route"
    length = len(truck.listPackages)
    while i < length:

        # Gets the next closest address
        next_address = closestAddress(next_package_address, truck.listPackages)

        next_package_address = int(next_address[2])
        truck.mileage = truck.mileage + float(next_address[0])
        truck.load = len(truck.listPackages)
        time = truck.departureTime + (float(truck.mileage) / float(truck.speed))

        folium.Marker(location=[next_address[3], next_address[4]],
                      popup=str(next_address[1]), icon=folium.Icon(color=str(marker), icon='bus')).add_to(map_delivery)

        truck.points.append([next_address[3], next_address[4]])

        # Removes delivered package from truck
        if str(next_address[1]) in truck.listPackages:
            truck.listPackages.remove(str(next_address[1]))
            current_package = myHash.get(next_address[1])

        current_package.delivery_time = decToTime(time)
        current_package.enroute_time = float(truck.departureTime)
        current_package.status = "Delivered"
        i = i + 1

        # Returns mileage, end time and total time if package list is empty
        if len(truck.listPackages) == 0:
            truck.mileage = truck.mileage + getDistance(0, next_package_address)
            truck.end_time = decToTime(truck.departureTime + float(truck.mileage) / float(truck.speed))
            truck.totalTime = decToTime(float(truck.mileage) / float(truck.speed))
            folium.PolyLine(np.array(truck.points, dtype=float), color=str(marker)).add_to(map_delivery)


# Calling delivering methods on the trucks
delivering(truck1, "red")
delivering(truck2, "blue")

# Truck 3 departures only when truck 1 arrives back at the depot
truck3.departureTime = min(timeToDec(truck1.end_time), timeToDec(truck2.end_time))
delivering(truck3, 'green')

class main:
    # User interface
    print("")
    print("Welcome to The Western Governors University Parcel Service (WGUPS) Terminal \n")

    # Prints Truck information
    print("Truck 1| departure time: ", decToTime(truck1.departureTime), "| End time:", truck1.end_time,
          " | Total delivery time: ", truck1.totalTime, " hours | Total mileage: ", round(truck1.mileage, 1),
          "| Load: ",
          truck1.maxNumberPackages)
    print("Truck 2| departure time: ", decToTime(truck2.departureTime), "| End time:", truck2.end_time,
          " | Total delivery time: ", truck2.totalTime, " hours | Total mileage: ", round(truck2.mileage, 1), "| Load: ",
          truck2.maxNumberPackages)
    print("Truck 3| departure time: ", decToTime(truck3.departureTime), "| End time:", truck3.end_time,
          "| Total delivery time: ", truck3.totalTime, " hours | Total mileage: ", round(truck3.mileage, 1), "| Load: ",
          truck3.maxNumberPackages)
    print("Combined Total Mileage = ", round((truck1.mileage + truck2.mileage + truck3.mileage), 1), "\n")

    while True:
        # If input is 1 it will look up packages, if 0 quits the program
        choice0 = input("To look up a package(s) enter 1. To quit enter 0 \n")
        if choice0 == "0":
            exit()
        elif choice0 != "1" and choice0 != "0":
            print("Error: input not valid \n")
            continue
        elif choice0 == "1":
            # Asks to input time
            choice15 = input("Enter a time to check the package(s) (please use HH:mm format in military time): " "\n")
            point_time = timeToDec(choice15)
            if not point_time:
                continue
            # if input is 0 will print all packages, if input is 1 then will print a specific package
            choice2 = input("For all packages enter 0, for a specific package enter 1: " "\n")
            if choice2 == "0":
                for i in range(1, 41):
                    package = myHash.get(int(i))
                    package.change_status(point_time, timeToDec(package.delivery_time))
                    print(myHash.get(i), "\n")
                mapChoice = input("See Deliveries on map enter Y/N\n")
                if mapChoice == "Y":
                    map_delivery.show_in_browser()

            elif choice2 == "1":
                choice3 = input("Enter package ID: \n")
                package = myHash.get(int(choice3))
                package.change_status(point_time, timeToDec(package.delivery_time))
                print(myHash.get(int(choice3)), "\n")
            elif choice2 != "1" and choice0 != "0":
                print("Error: input not valid \n")
                continue
