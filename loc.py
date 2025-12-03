import folium
import requests

def get_location(imei):
    api_key = '7f3d21e467ab4133b125ef36c8f08e56' # Remplace avec ta clé API Telma
    url = f'https://api.opencagedata.com/geocode/v1/json?q={imei}&key={api_key}'  # Utilise l'IMEI comme requête

    try:
        response = requests.get(url)
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            # Récupère les coordonnées de la première résultat
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            print(f' {latitude} et {longitude}')
            return latitude, longitude
        else:
            print("Aucun résultat trouvé pour cet IMEI.")
            return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

imei = '358327091324850/61'  # Remplace avec le numéro IMEI de ton téléphone
coordinates = get_location(imei)
if coordinates:
    print(f"Coordonnées GPS: Latitude {coordinates[0]}, Longitude {coordinates[1]}")
else:
    print("Impossible d'obtenir les coordonnées pour cet IMEI.")
maop = folium.Map(location=[coordinates[0], coordinates[1]], zoom_start=12)
folium.Marker([coordinates[0], coordinates[1]], popup=coordinates[0]).add_to(maop)
maop.save("D:/bd/map.html")
