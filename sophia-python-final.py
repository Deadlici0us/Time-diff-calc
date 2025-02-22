# Installation: pip install geopy requests timezonefinder tzlocal pytz
# Import necessary libraries for geocoding, timezone finding, and working with datetime and timezones
from geopy.geocoders import Nominatim  # For geocoding (getting latitude and longitude from location names)
from timezonefinder import TimezoneFinder  # For finding the timezone based on latitude and longitude
from tzlocal import get_localzone  # For getting the local system timezone
import datetime  # For working with dates and times
import pytz  # For working with timezones

# Define a class for geocoding using Nominatim
class NominatimGeocoder:
    # Method to get latitude and longitude from a location name
    def geocode(self, location_name):
        # Create a geolocator instance with a user agent (required by Nominatim API)
        geolocator = Nominatim(user_agent="sophia-python-final")  # Create Nominatim object with custom user agent
        # Return the geocoded location (latitude and longitude)
        return geolocator.geocode(location_name)

# Define a class for finding time zones
class TZFinder:
    def __init__(self):
        self.tf = TimezoneFinder()  # Initialize the TimezoneFinder instance
        
    # Method to get the time zone based on latitude and longitude
    def get_timezone(self, latitude, longitude):
        # Use TimezoneFinder to get the timezone at the given coordinates
        return self.tf.timezone_at(lng=longitude, lat=latitude)

# Define a class for getting location details, including time zone and time difference
class LocationInfo:
    # Constructor to initialize geocoder and timezone finder instances
    def __init__(self, geocoder, timezone_finder):
        # Store the geocoder instance
        self._geocoder = geocoder
        # Store the timezone finder instance
        self._timezone_finder = timezone_finder

    # Method to get location details (including time zone and time difference) for a given location name
    def get_location_details(self, location_name):
        # Get the geocoded location (latitude and longitude) for the location name
        location = self._geocoder.geocode(location_name)
        # Check if the location was found
        if location:
            # Extract latitude and longitude from the location object
            latitude = location.latitude
            longitude = location.longitude
            # Get the timezone for the coordinates using the timezone finder
            timezone = self._timezone_finder.get_timezone(latitude, longitude)

            # Check if a valid timezone was found
            if timezone:
                # Create a timezone object for the location using pytz
                tz = pytz.timezone(timezone)

                # Get the local system time (current time in the local timezone)
                local_time = datetime.datetime.now(get_localzone())
                # Get the time for the location using the timezone object
                location_time = datetime.datetime.now(tz)

                # Get the UTC offset (in hours) for the location's time
                location_offset = location_time.utcoffset().total_seconds() / 3600
                # Get the UTC offset (in hours) for the local system time
                local_offset = local_time.utcoffset().total_seconds() / 3600

                # Calculate the time difference in hours (local time offset - location time offset)
                time_difference_hours = local_offset - location_offset 

                # Return a dictionary containing location details and time difference
                return {
                    "\nLocal time": local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),  # Local time with timezone info
                    "\nLocation": location.address,  # Address of the location
                    "Latitude": latitude,  # Latitude of the location
                    "Longitude": longitude,  # Longitude of the location
                    "Location time": location_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),  # Location's local time with timezone info
                    "\nTime difference with local time": f"{time_difference_hours:.1f} hours\n"  # Time difference with local time (in hours)
                }
            else:
                # If timezone not found, return a message
                print("Time zone not found. Please try again.")
                return None
        else:
            # If location not found, return a message
            print("Location not found. Please try again.")
            return None

# Create instances of geocoder and timezone finder
geocoder = NominatimGeocoder()
timezone_finder = TZFinder()

print("\n\n#####################################")
print("#     Time difference calculator    #")
print("#####################################")

# Create an instance of LocationInfo using dependency injection (pass geocoder and timezone finder instances)
location_info_obj = LocationInfo(geocoder, timezone_finder)
while True:
    # Prompt the user to enter a location (city or country name)
    print("\nPress CTRL^C to exit")
    location_name = input("\nEnter a location to calculate (e.g., city, country name like 'Paris', 'USA'): ")

    # Get location details (including time zone and time difference)
    location_details = location_info_obj.get_location_details(location_name)

    # Check if location details are available
    if location_details:
        # Print location details
        for key, value in location_details.items():
            print(f"{key}: {value}")            