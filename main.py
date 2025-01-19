'''
Name : Dongok Yang
Date : 2025-01-17
Class : ADEV-3005(261246)
'''
# Import required libraries
from requests import get
import json
from PIL import Image
from io import BytesIO
from menu import Menu

# API key for accessing NASA photos
API_KEY = 'luqFf5EMzwZ3CWeUziGQJLyP1mEFfmefVtRuJgFh'

# Variable to keep the current image page
current_image = 1

# display an image
def display_photo(url):
 """Displays the photo found at url."""
 img_resp = get(url)
 img = Image.open(BytesIO(img_resp.content))
 img.show()
 img.close()

# Display photos with navigation options
def display_photos(photos):
    global current_image

    # Display photos in the current range
    if current_image > len(photos):
        print("\nNo more images to show. Choose [p] to go back")
    else:
        print("\nAvailable photos:")
        for idx, photo in enumerate(photos[current_image:current_image + 10], current_image + 1):
            print(f"{idx-1}: Camera - {photo['camera']['full_name']}")

    # Navigation and photo selection
        print("Options:")
        print(" [n] Next page")
        print(" [p] Previous page")
        print(" [b] Back to main menu")
        print(f" [{idx-10} ~ {idx-1}] show image")

    photo_choice = input("\nChoose a photo by number or use the navigation options: ").lower()

    if photo_choice == 'b':
        return False
    elif photo_choice == 'n':
        current_image += 10
        return True
    elif photo_choice == 'p':
        if current_image >= 10:
            current_image -= 10
        else:
            print("\nYou are already on the first page.")
        return True

    try:
        photo_index = int(photo_choice) - 1
        if 0 <= photo_index < len(photos):
            photo_url = photos[photo_index]['img_src']
            display_photo(photo_url)
        else:
            print("\nInvalid choice. Please choose a valid photo number.")
        return True
    except ValueError:
        print("\nInvalid input. Please enter a number or a valid navigation option.")
        return True


# Function for Curiosity rover
def Curiosity():
    print("Curiosity rover is selected")
    selectedRover = 'curiosity'
    date = input("select the date in the following format (YYYY-MM-DD)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()

    if all_rovers.get('photos'):
        photos = all_rovers['photos']
        while display_photos(photos):
            pass
    else:
        print("No photos found for this date.")

# Function for Opportunity rover
def Opportunity():
    print("Opportunity rover is selected")
    selectedRover = 'opportunity'
    date = input("select the date in the following format (YYYY-MM-DD)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()
    if all_rovers.get('photos'):
        photos = all_rovers['photos']
        while display_photos(photos):
            pass
    else:
        print("No photos found for this date.")

# Function for Spirit rover
def Spirit():
    print("Spirit rover is selected")
    selectedRover = 'spirit'
    date = input("select the date in the following format (YYYY-MM-DD)")
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{selectedRover}/photos?earth_date={date}&api_key={API_KEY}"
    all_rovers = get(url_rovers).json()
    if all_rovers.get('photos'):
        photos = all_rovers['photos']
        while display_photos(photos):
            pass
    else:
        print("No photos found for this date.")

# Main menu with rover options
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