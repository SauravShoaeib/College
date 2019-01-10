#Saurav Hossain
#09/21/18
#A program that uses folium to make a map of New York City centered at (40.75, -74.125)

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')
