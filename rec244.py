import requests


def localiser_ip(adresse_ip, api_key):
    url = f"http://api.ipstack.com/{adresse_ip}?access_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Pays :", data.get("country_name"))
        print("Ville :", data.get("city"))
        print("Latitude :", data.get("latitude"))
        print("Longitude :", data.get("longitude"))
    else:
        print("Erreur lors de la requête à l'API.")


# Exemple d'utilisation
adresse_ip_a_localiser = "192.168.7.2"  # Remplacez par l'adresse IP que vous souhaitez localiser
cle_api = "YOUR_API_KEY"  # Remplacez par votre clé d'API

localiser_ip(adresse_ip_a_localiser,cle_api)
