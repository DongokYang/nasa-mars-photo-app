'''
Name : Dongok Yang
Date : 2025-01-17
Class : ADEV-3005(261246)
'''
from requests import get
import json
from PIL import Image
from io import BytesIO
from menu import Menu


API_KEY = 'luqFf5EMzwZ3CWeUziGQJLyP1mEFfmefVtRuJgFh'

def display_photo(url):
 """Displays the photo found at url."""
 img_resp = get(url)
 img = Image.open(BytesIO(img_resp.content))
 img.show()
 img.close()

def Curiosity():
    print("Curiosity rover is selected")
    selectedRover = 'curiosity'
    date = input("select the date in the following format (xxxx-xx-xx)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()
    print(all_rovers)

def Opportunity():
    print("Opportunity rover is selected")
    selectedRover = 'opportunity'
    date = input("select the date in the following format (xxxx-xx-xx)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()
    print(all_rovers)

def Spirit():
    print("Spirit rover is selected")
    selectedRover = 'spirit'
    date = input("select the date in the following format (xxxx-xx-xx)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()
    print(all_rovers)

main_menu = Menu(
    title="Main Menu",
    options=[
        ("Curiosity rover", Curiosity),
        ("Opportunity rover", Opportunity),
        ("Spirit rover", Spirit),
        ("Exit", Menu.CLOSE)
    ],
    prompt=">> "
)

main_menu.open()