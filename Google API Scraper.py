import pandas as pd
import numpy as np
import time
import googlemaps
import re

excel_file = r"## PATH FOR XLSX FILE WITH 'Address' column.xlsx ##"
df = pd.read_excel(excel_file)
search = df['Address']

gmaps = googlemaps.Client(key='## Google API Key ##')

new_file = []

try:
    for location in search:
        try:
            geocode_result = gmaps.geocode(location)
            result = str(geocode_result)
            loc = re.search(r"(?:'location': {'lat': ([-.0-9]*), 'lng': ([-.0-9]*))", result)
            lat = str(loc.group(1))
            lng = str(loc.group(2))
            new_line = str(location) + '|' + str(lat) + '|' + str(lng)
            new_file.append(new_line)
            
        except:
            new_line = str(location) + '|error'
            new_file.append(new_line)
        print(new_line)
except:
    pass

csvexport = pd.DataFrame([sub.split('|') for sub in new_file], columns =['Address', 'Latitude', 'Longitude'])
doc = r"## PATH FOR XLSX FILE OUTPUT.xlsx ##"
writer = pd.ExcelWriter(doc, engine='xlsxwriter')
csvexport.to_excel(writer, sheet_name='Sheet1', startrow=0)
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
writer.save()
