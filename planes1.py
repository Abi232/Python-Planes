"""
    Find some interesting information in flight vectors
    ...
"""

import math
import json

def haversine(lat1, lon1, lat2, lon2):
    """
    Haversine Formula - Distance between two GPS points)
    :param lat1: latitude of the 1st point
    :param lon1: longitude of the 2nd point
    :param lat2: latitudes of the 2nd point
    :param lon2: longitude of the 2nd point
    :return: distance between latitudes and longitudes in kilometers
    """
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


def highest_plane(vectors): 
        Highest_plane = vectors[0] #assumes the first plane is the highest
        for i in vectors: # iterating over the list of vectors
            if i['geo_altitude'] > Highest_plane['geo_altitude']: # compares the previous to the next plane
                Highest_plane = i # setting the new lowest plane
        return(f"Highest flying plane: {Highest_plane['callsign']}at {Highest_plane['geo_altitude']} meters.") # returns the value

def lowest_plane(vectors):
        Lowest_plane = vectors[0] # assumes the first plane is the lowest ie the correct answer
        for i in vectors: # iterates over the composite list of vectors
            if i["geo_altitude"] < Lowest_plane["geo_altitude"]: #comparing the previous plane to the next
                Lowest_plane = i # sets the new lowest plane as the answer
        return(f"Lowest flying plane: {Lowest_plane['callsign']}at {Lowest_plane['geo_altitude']} meters. ") # returns the value


def fastest_climber(vectors):
        Fastest_ascender = vectors[0] #assumes the first plane is the fastest climber
        for i in vectors: #iterates over the list of vectors
            if i["vertical_rate"] > Fastest_ascender["vertical_rate"]: #compares the vertical rates of the planes
                Fastest_ascender = i #sets the new fastest climber as the answer
        return(f"Fastest ascending plane: {Fastest_ascender['callsign']} at {Fastest_ascender['vertical_rate']} meters per second.") #returns the correct value


def fastest_descender(vectors):
        Fastest_descender = vectors[0] #assumes the first plane is the fastest descender
        for i in vectors: #iterates over the list of vectors
            if i["vertical_rate"] < Fastest_descender['vertical_rate']: #compares the vertical rates to find the fastest descending
                Fastest_descender = i # sets the new fastest descender as the answer
        return(f"Fastest descending plane: {Fastest_descender['callsign']} at {Fastest_descender['vertical_rate']} meters per second.") # returns the value


def closest_to_ERAU(vectors):
    
    Closest_to_ERAU = vectors[0] # assumes the first plane is the closest to ERAU
    ERAU_Latitude = 34.61741925787892 # riddle latitude
    ERAU_Longitude = -112.45050454448898 #riddle longitude
    distance = haversine(ERAU_Latitude, ERAU_Longitude, Closest_to_ERAU['latitude'], Closest_to_ERAU['longitude']) # uses haversine to set the distance to compare the coordinates to
    for i in vectors: #iterates over the list of vectors
        if haversine(ERAU_Latitude, ERAU_Longitude, i['latitude'], i['longitude']) < distance: # compares the coordinates of the vectors to the ERAU lat and long to find the distance
            distance = haversine(ERAU_Latitude, ERAU_Longitude, i['latitude'], i['longitude']) #finds the least distance in the vectors
            Closest_to_ERAU = i #sets the closest to ERAU as the answer
    return(f"Closest to ERAU : {Closest_to_ERAU['callsign']} at {round(distance)} km away.") #returns the value



def closest_planes(vectors):
    plane_1 = vectors[0] # assumes the first plane is the lowest ie the correct answer
    for i in vectors: # iterates over the composite list of vectors
        if i['latitude']: i['longitude'] < plane_1['latitude'], plane_1['longitude'] #comparing the previous plane to the next
        plane_1 = i # sets the new lowest plane as the answer
        plane_2 = vectors[1]
    #Finds the lowest flying plane based on the 'geo_altitude'
   # :param vectors: list of dictionaries (flight vectors of planes)
    #:return: a tuple containing the two airplanes closest to each other and their distance
        for j in vectors:
            if i["latitude"]: i['longitude'] < plane_2["latitude"], plane_2['longitude']
            distance = haversine(i['latitude'], i['longitude'], j['latitude'], j['longitude'])
            plane_2 = j
        return(f"Closest planes to each other : {plane_1['callsign']} and {plane_2['callsign']} at {round(distance)} km away from each other.")

            
    # return plane_1, plane_1, round(distance)

with open('vectors.json', 'r') as fh:
    vectors = json.load(fh)

print("Flight Vector Analysis:")
lowest = lowest_plane(vectors)
print(lowest)

highest = highest_plane(vectors)
print(highest)

fastest = fastest_descender(vectors)
print(fastest)
closest = closest_to_ERAU(vectors)
print(closest)
Closest = closest_planes(vectors)
print(Closest)