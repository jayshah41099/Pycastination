from geopy.geocoders import Nominatim

# using Nominatin API
geolocator = Nominatim(user_agent="geoapiExercises")

# zipcode input
a = input("enter the zipcode : ")
zipcode = a

#Using geocode
location = geolocator.geocode(zipcode)

# displaying address details
print("zipcode: ", zipcode)
print("Details of the zipcode: \n", location)