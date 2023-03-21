from math import sin, cos, acos, radians
import requests
import urllib.parse

def getCoordsRequest(userPostcode):
    if userPostcode == "":
        return {"status":"no_match"}
    url = urllib.parse.quote("api.getthedata.com/postcode/" + userPostcode)
    url = "https://" + url
    print(url)
    response = requests.get(url)
    response = response.json()
    return response

def getLatLon(postcode):
    location = getCoordsRequest(postcode)
    if location["status"] == "match" and location["match_type"] == "unit_postcode":
        lat, lon = float(location["data"]["latitude"]), float(location["data"]["longitude"])
        return lat, lon
    else:
        return None, None
            
def getDistance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
    EARTH_RADIUS = 6371 # km
    distance = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon2-lon1))*EARTH_RADIUS
    return distance