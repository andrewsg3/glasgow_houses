"""
WP1: Scrape data from rightmove
Refer to bs4 documentation for usage: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import requests
from bs4 import BeautifulSoup

def rightmove_title(url):
    """
    Demonstration of web scraping / interpreting pipeline, only makes use of title (which can be pretty useful!)
    """
    print("\nScraping "+url)
    data = {"beds":[], "postcode":[], "address":[],"flat_position":[],"floor":[]}

    ## Get HTML from website
    r = requests.get(url)   
    html_doc = r.text

    ## Parse with bs4
    soup =  BeautifulSoup(html_doc, 'html.parser')
    title = soup.title.string
    #print(title)

    ## Use regex to pull info from title
    import re
    try:
        regex = '[0-9]'
        beds = re.search(regex, title).group(0)
        #print(f"Beds: {beds}")
        data["beds"] = beds
    except:
        pass

    try:
        regex = 'G42.[^\s,]*'
        postcode = re.search(regex, title).group(0)
        #print(f"Postcode: {postcode}")
        data["postcode"] = postcode
    except:
        pass

    try:
        regex = '[0-9]*.[A-Z][a-z]*.[A-Z][a-z]*'
        address = re.search(regex, title).group(0)
        #print(f"Address: {address}")
        data["address"] = address
    except:
        pass

    try:
        regex = '[0-9]/[0-9]'
        flat_position = re.search(regex, title).group(0)
        #print(f"Flat position: {flat_position}")
        data["flat_position"] = flat_position

        floor = {
            "0":"Ground",
            "1":"1st",
            "2":"2nd",
            "3":"Top"
        }

        flr = floor[flat_position[0]]
        #print(f"Floor: {flr}")
        data["floor"] = flr

    except:
        pass

    return data

    

# Usage 
#rightmove_title("https://www.rightmove.co.uk/properties/110163125#/?channel=RES_BUY")
#rightmove_title("https://www.rightmove.co.uk/properties/88139002#/?channel=RES_BUY")


## Trying to get the property description from here
r = requests.get("https://www.rightmove.co.uk/properties/110163125#/?channel=RES_BUY")
html_doc = r.text
soup =  BeautifulSoup(html_doc, 'html.parser')

## Write prettified stuff to file, for visual interpretation.
with open('property_html.txt', 'w') as f:
    f.write(soup.prettify()) 