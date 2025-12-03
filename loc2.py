import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

num = "+261341178920"
# clef="7f3d21e467ab4133b125ef36c8f08e56"
# clef="1fcede428931ea4d65e2645ba4be4c68"
clef = "61899b68e1d0451aa5286f881784b591"
monnum = phonenumbers.parse(num)
loc = geocoder.description_for_number(monnum, "fr")
print(loc)
print(carrier.name_for_number(monnum, 'fr'))

coord = OpenCageGeocode(clef)
requ = str(loc)
rep = coord.geocode(requ)
lat = rep[0]["geometry"]["lat"]
long = rep[0]["geometry"]["lng"]
print(rep)
print(lat, long)
maop = folium.Map(location=[lat, long], zoom_start=12)
folium.Marker([lat, long], popup=loc).add_to(maop)
maop.save("D:/bd/map.html")
