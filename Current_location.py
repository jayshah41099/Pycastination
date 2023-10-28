# Requirement : pip install geopy
# command : python3 Current_location.py

from geopy.geocoders import Nominatim

def get_current_location():
    # Initialize Nominatim geolocator
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Get the current location based on IP address
    location = geolocator.geocode('my location', timeout=10)

    if location:
        print(f"Your current address is: {location.address}")
    else:
        print("Location not found.")

if __name__ == "__main__":
    get_current_location()
