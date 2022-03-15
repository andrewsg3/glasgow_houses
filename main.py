"""
Main file from which all other modules will be utilised.
"""
## (1) Imports


## (2) Scrape primary data from rightmoves
from scraper import rightmove_title
url = "https://www.rightmove.co.uk/properties/88139002#/?channel=RES_BUY"
data = rightmove_title(url)
print(data)


## (3) Scrape secondary data (coordinates, sale price)
from coords import coords
postcode = data["postcode"]
coordinates = coords(postcode)
print(f"Coordinates of property at {postcode}: {coordinates}")

import saleprice
price = None
print(f"Sale price of property at {postcode}: {price}")

## (4) Clean data


## (5) ML Model training 


## (6) ML Model inference