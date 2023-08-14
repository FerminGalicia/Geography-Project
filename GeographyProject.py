# ME21 Project One, python.
# In this program, the user will ask for season and weather recommendations and obtain the output of the top five travel destinations.

# This code will define the Haversine formula to calculate the distance along with longitude and latitude.
# Thus, the following variables "UCMlong" and "UCMlat" will represent the latitude and longitude of point one to point two.

def haversine(UCMlong, UCMlat, Long, Lat):
    UCMlong, UCMlat, Long, Lat = map(radians, [UCMlong, UCMlat, Long, Lat])
    Distlong = Long - UCMlong
    Distlat = Lat - UCMlat
    
    # This code displays the Haversine formula to have following above variables including the radius of 6360 km.
    a = sin(Distlat / 2) ** 2 + cos(UCMlat) * cos(Lat) * sin(Distlong / 2) ** 2
    return 2 * 6360 * asin(sqrt(a))

# This code will import the math variables given above and display them into the formula.
from math import radians, sin, cos, asin, sqrt

# This code will open the file that contains the details of the listed cities.
filename = open('cities.txt', 'r')

# This code will ask whether the user wants cold or warm weather for their desired travel by making the input a string.
climate = input('Are you searching for cold or warm weather?' )
climate = str(climate)

# This code displays a loop for the desired weather.
if climate != 'cold' and climate != 'warm':
    print('That is not an option!')
    raise SystemExit

# This code displays whether the user wants to travel during summer or winter by making it a string as well.
Season = input('Are you searching for winter or summer travel?')
Season = str(Season)

# Just in case the user enters an incomprehensible word, the output will read it as a rejection.
# The user should not capitalize any words when answering the questions.
if Season != 'winter' and Season != 'summer':
    print('The entered value does not exist. Try again!')
    # This code displays a system exit where it will end the overall coding of this program.
    raise SystemExit

# This code will display a list to order the details of the file.
explicitData = []

# This code will allow the file to read off of every line of data.
for row, line in enumerate(filename):
    rates = line.strip().split('\t')
    if row != 0:
        explicitData.append(rates)
filename.close()

# This code will display UC Merced's longitude and latitude to be 120 and 37.
UCMlong = 120
UCMlat = 37

# This code will put in order the data of the desired user's inputs.
citylist = []

# For this partial section, this lengthy code will display the longitude's set of values to be ordered.
# It will aso help in determining whether the code will read on any specified city's position.
for set in explicitData:
    list = []
    longSet = set[1]
    if longSet[2] == '0' or longSet[2] == '1' or longSet[2] == '2' or longSet[2] == '3' or longSet[2] == '4' or longSet[2] == '5' or longSet[2] == '6' or longSet[2] == '7' or longSet[2] == '8' or longSet[2] == '9':
        if longSet[1] == '0' or longSet[1] == '1' or longSet[1] == '2' or longSet[1] == '3' or longSet[1] == '4' or longSet[1] == '5' or longSet[1] == '6' or longSet[1] == '7' or longSet[1] == '8' or longSet[1] == '9':
            Long = (longSet[0:3])
        else:
            Long = longSet[0:1]
    elif longSet[1] == '0' or longSet[1] == '1' or longSet[1] == '2' or longSet[1] == '3' or longSet[1] == '4' or longSet[1] == '5' or longSet[1] == '6' or longSet[1] == '7' or longSet[1] == '8' or longSet[1] == '9':
        Long = longSet[0:2]
    Long = int(Long)
    if longSet[6:] == 'E':
        Long = -Long
    elif longSet[5:] == 'E':
        Long = -Long
    elif longSet[4:] == 'E':
        Long = -Long

    # For this partial part of the code, it will do the same method as above. Both parts contain loops.
    latSet = set[0]
    if latSet[1] == '0' or latSet[1] == '1' or latSet[1] == '2' or latSet[1] == '3' or latSet[1] == '4' or latSet[1] == '5' or latSet[1] == '6' or latSet[1] == '7' or latSet[1] == '8' or latSet[1] == '9':
        Lat = latSet[0:2]
    else:
        Lat = latSet[0:1]
    Lat = int(Lat)
    if latSet[5:] == 'S':
        Lat = -Lat
    elif latSet[4:] == 'S':
        Lat = -Lat

    # This code will determine the desired season based on the latitudes by adding loops.
    if Season == 'winter':
        if Lat > 35 or Lat < -66:
            citiesClimate = 'cold'
        if Lat <= 35 and Lat >= -66:
            citiesClimate = 'warm'
    if Season == 'summer':
        if Lat > 66 or Lat < -35:
            citiesClimate = 'cold'
        elif Lat <= 66 and Lat >= -35:
            citiesClimate = 'warm'

    # This code will use the Haversine formula to determine the two points between UCM and the desired city the user inputs.
    # Furthermore, this code will create a list to store the user's input based on the season and weather.
    if citiesClimate == climate:
        distFormula = haversine(UCMlong, UCMlat, Long, Lat)
        list.append(distFormula)
        list.append(set[2])
        list.append(set[3])
        list.append(set[4])
        citylist.append(list)

citylist.sort()

# For the final part of this program, this sectioned code will order the outputs based on the user's information from least to greatest.
# Therefore, the code will give the user the best five choices of where to travel from UC Merced.

endingPointA = []
endingPointA.extend(citylist[0])
endingPointB = []
endingPointB.extend(citylist[1])
endingPointC = []
endingPointC.extend(citylist[2])
endingPointD = []
endingPointD.extend(citylist[3])
endingPointE = []
endingPointE.extend(citylist[4])

# This final part will print out the displayed cities that will fit best to the user.
print('Here are your best five destinations from what you desire:')
print(endingPointA[1:4])
print(endingPointB[1:4])
print(endingPointC[1:4])
print(endingPointD[1:4])
print(endingPointE[1:4])




