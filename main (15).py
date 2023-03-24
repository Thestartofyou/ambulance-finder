import googlemaps
import time

# Set up the Google Maps API client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Define the location of the ambulance you want to follow
ambulance_location = '123 Main St, Anytown, USA'

# Continuously poll the Google Maps API for the location of the ambulance
while True:
    # Get the current location of the ambulance
    ambulance_data = gmaps.geocode(ambulance_location)
    ambulance_lat = ambulance_data[0]['geometry']['location']['lat']
    ambulance_lng = ambulance_data[0]['geometry']['location']['lng']
    
    # Do something with the ambulance location data, such as display it on a map
    print(f'Ambulance location: ({ambulance_lat}, {ambulance_lng})')
    
    # Wait a certain amount of time before polling again
    time.sleep(5)
