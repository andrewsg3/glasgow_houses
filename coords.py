"""
WP2: Use postcode to gain geopositional information
Achieved via https://postcodes.io/ API 
"""
import requests 

def coords(postcode):
    ## Obtain JSON from API
    api_address = "http://api.postcodes.io/postcodes/"
    url = api_address + postcode
    r = requests.get(url)   
    #print(f"\nResponse from API for {postcode}:\n")
    #print(r.json())
    #print("\n")

    ## Parse JSON
    data =  r.json()["result"]
    long = data["longitude"]
    lat = data["latitude"]
    #print(f"Coordinates for {postcode}: ({lat}, {long})")
    return [lat, long]

## Example
#print(coords("G412DN"))