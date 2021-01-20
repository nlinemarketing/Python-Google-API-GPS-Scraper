# Python-GPS-Scraper

Python GPS Scraper is a simple way to parse Google Maps API data to get Longitude & Latitude from a full address. Designed this project to create an easy solution for uploading GPS POIs to Garmin GPS navigator.  

Instead of making individual requests to the Google Maps API, we can make a for loop to make these requests, then parse the JSON  with Regex to extract Lng & Lat, and have them exported to Excel for uploading to Garmin GPS navigator. 

Python GPS Scraper runs on python3

## Dependancies
[Pandas](https://pandas.pydata.org/)
[Numpy](https://numpy.org/doc/stable/)
[Googlemaps](https://github.com/googlemaps/google-maps-services-python) 
[Re](https://docs.python.org/3/library/re.html)  

## Requirements
Each Google Maps Web Service request requires an API key or client ID. API keys
are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).

For even more information on getting started with Google Maps Platform and generating/restricting an API key, see [Get Started with Google Maps Platform](https://developers.google.com/maps/gmp-get-started) in our docs.

**Important:** This key should be kept secret on your server.

## Configuration
Replace ## Google API Key ## with your API Key

Add file paths for ## PATH FOR XLSX FILE OUTPUT.xlsx ## & ## PATH FOR XLSX FILE WITH 'Address' column.xlsx ## these files will need complete path ending in .xlsx

## Load data to Garmin
[How to POI Loader](https://github.com/googlemaps/google-maps-services-python)
[POI Loader Step-by-step](http://www.go2poi.com/guide/garmin.php)
[POI File Converter](https://www.gps-data-team.com/convert.php)
