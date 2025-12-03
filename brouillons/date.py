from datetime import datetime


now = datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')
# Afficher la date et l'heure formatées
print(f'Date et heure formatées : {formatted_date_time}')
