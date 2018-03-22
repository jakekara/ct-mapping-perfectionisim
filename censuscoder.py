import requests
import urllib
import re

def geocode(addrstr, benchmark=9):

    # Geocode an address-ish string to lat long using Census API:   
    #  https://geocoding.geo.census.gov/geocoder/

    endpoint = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address="

    url = re.sub(r"\s+", '+', endpoint + addrstr + "&benchmark=" + str(benchmark)+ "&format=json")

    return requests.get(url).json()
    
    