"""
This is a program to find location by ZIP code and ZIP code by location,
as well as to calculate the distance between to ZIP codes.

U.S. ZIP code is a five-digit integer number.
Location is given by the name of a city/town and a two-letter abbreviation
of the state.

Sample Execution:
-----------------

Command ('loc', 'zip', 'dist', 'end') => loc
loc

Enter a ZIP Code to lookup => 32963
32963
ZIP Code 32963 is in Vero Beach, FL, Indian River county,
coordinates: (027°41'23.23"N,080°22'32.61"W)


Command ('loc', 'zip', 'dist', 'end') => zip
zip

Enter a city name to lookup => Orlando
Orlando

Enter the state name to lookup => FL
FL
The following ZIP Code(s) found for Orlando, FL: 32801, 32802, 32803, 32804, 32805, 32806, 32807, 32808, 32809, 32810, 32811, 32812, 32814, 32815, 32816, 32817, 32818, 32819, 32820, 32821, 32822, 32824, 32825, 32826, 32827, 32828, 32829, 32830, 32831, 32832, 32833, 32834, 32835, 32836, 32837, 32839, 32853, 32854, 32855, 32856, 32857, 32858, 32859, 32860, 32861, 32862, 32867, 32868, 32869, 32872, 32877, 32878, 32886, 32887, 32890, 32891, 32893, 32897, 32898, 32899


Command ('loc', 'zip', 'dist', 'end') => dist
dist

Enter the first ZIP Code => 12180
12180

Enter the second ZIP Code => 32963
32963
The distance between 12180 and 32963 is 1102.72 miles


Command ('loc', 'zip', 'dist', 'end') => end
end

Done

Course: Python
Author(s): Konstantin Kuzmin
Date: 2/19/2019, modified 12/16/2021
"""

import util
import math
import logging.handlers


def calculate_distance(location1, location2):
    """
    This function returns the great-circle distance between location1 and
    location2.

    Parameters:
    location1 (iterable): The geographic coordinates
    of the first location. The first element of the iterable is latitude,
    the second one is longitude.

    location2 (iterable): The geographic coordinates
    of the second location. The first element of the iterable is latitude,
    the second one is longitude.

    Returns:
    float: Value of the distance between two locations computed using
    the haversine formula
    """

    lat1 = math.radians(location1[0])
    lat2 = math.radians(location2[0])
    long1 = math.radians(location1[1])
    long2 = math.radians(location2[1])
    del_lat = (lat1 - lat2) / 2
    del_long = (long1 - long2) / 2
    angle = math.sin(del_lat)**2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(del_long)**2
    distance = 2 * 3959.191 * math.asin(math.sqrt(angle))
    return distance


def degree_minutes_seconds(location):
    minutes, degrees = math.modf(location)
    degrees = int(degrees)
    minutes *= 60
    seconds, minutes = math.modf(minutes)
    minutes = int(minutes)
    seconds = 60 * seconds
    return degrees, minutes, seconds


def format_location(location):
    ns = ""
    if location[0] < 0:
        ns = 'S'
    elif location[0] > 0:
        ns = 'N'

    ew = ""
    if location[1] < 0:
        ew = 'W'
    elif location[0] > 0:
        ew = 'E'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(location[0]))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(location[1]))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'


def zip_by_location(codes, location):
    zips = []
    for code in codes:
        if location[0].lower() == code[3].lower() and \
           location[1].lower() == code[4].lower():
            zips.append(code[0])
    return zips


def location_by_zip(codes, zipcode):
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()


def process_loc(codes):
    zipcode = input('Enter a ZIP Code to lookup => ')
    print(zipcode)
    location = location_by_zip(codes, zipcode)
    if len(location) > 0:
        print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: {}'.
              format(zipcode, location[2], location[3], location[4],
                     format_location((location[0], location[1]))))
    else:
        print('Invalid or unknown ZIP Code')


def process_zip(codes):
    city = input('Enter a city name to lookup => ')
    print(city)
    city = city.strip().title()
    state = input('Enter the state name to lookup => ')
    print(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))
    if len(zipcodes) > 0:
        print('The following ZIP Code(s) found for {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        print('No ZIP Code found for {}, {}'.format(city, state))


def process_dist(codes):
    zip1 = input('Enter the first ZIP Code => ')
    print(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    logger.info(f'Received the first ZIP {zip1}')
    zip2 = input('Enter the second ZIP Code => ')
    print(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    logger.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        print('The distance between {} and {} cannot be determined'.
              format(zip1, zip2))
    else:
        dist = calculate_distance(location1, location2)
        print('The distance between {} and {} is {:.2f} miles'.
              format(zip1, zip2, dist))


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=5*1024*1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                        handlers=[rfh])
    logger = logging.getLogger('main')

    zip_codes = util.read_zip_all()

    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        print(command)
        command = command.strip().lower()
        if command == 'loc':
            process_loc(zip_codes)
        elif command == 'zip':
            process_zip(zip_codes)
        elif command == 'dist':
            process_dist(zip_codes)
        elif command != 'end':
            print("Invalid command, ignoring")
        print()
    print("Done")
    logging.shutdown()
