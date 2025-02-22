# Time Difference Calculator

This Python script calculates the time difference between the local system time and a user-provided location using geolocation and timezone data. This was made as part of "Introduction to Python" course.

## Features
- Automatically detects the local system timezone.
- Retrieves the timezone of a given location based on latitude and longitude.
- Computes the time difference between the local system and the target location.
- Displays formatted time details.

## Requirements
This script requires Python 3 and the following dependencies:
- `geopy`
- `timezonefinder`
- `tzlocal`
- `pytz`

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies using:
```sh
pip install geopy timezonefinder tzlocal pytz
```

## Usage
Run the script using:
```sh
python3 sophia-python-final.py
```
Then, enter the location when prompted:
```sh
Enter a location to calculate (e.g., city, country name like 'Paris', 'USA'): Buenos Aires
```
The output will display the location details and time difference:
```sh

Local time: 2025-02-22 14:40:16 UTC+0000

Location: Buenos Aires, Comuna 6, Ciudad Autónoma de Buenos Aires, Argentina
Latitude: -34.6083696
Longitude: -58.4440583
Location time: 2025-02-22 11:40:16 -03-0300

Time difference with local time: 3.0 hours

```
### Exit
Press `CTRL+C` to stop the script.

### License
This project is licensed under the MIT License.



