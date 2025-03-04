import requests
import ctypes
import os

# Voeg je Unsplash API-sleutel hier toe:
unsplash_api_key = "i1pq-CTFnVEdQqYb92VlonUcDI8E-cW1qsBMaLmiSGE"  # Jouw API-sleutel hier

# Functie om een random afbeelding op te halen van Unsplash
def get_unsplash_image():
    url = f"https://api.unsplash.com/photos/random?client_id={717560}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data[0]["urls"]["regular"]
        return image_url
    else:
        print("Er ging iets mis bij het ophalen van een afbeelding.")
        return None

# Functie om een afbeelding in te stellen als bureaubladachtergrond
def set_wallpaper(image_url):
    # Download de afbeelding
    image = requests.get(image_url, stream=True)
    if image.status_code == 200:
        image_path = "wallpaper.jpg"
        with open(image_path, "wb") as f:
            f.write(image.content)

        # Zet de afbeelding als achtergrond
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(image_path), 3)
    else:
        print("Er ging iets mis bij het downloaden van de afbeelding.")

# Haal de afbeelding op en stel deze in als achtergrond
image_url = get_unsplash_image()
if image_url:
    set_wallpaper(image_url)
