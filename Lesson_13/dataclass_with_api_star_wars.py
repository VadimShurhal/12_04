from pprint import pprint
import requests

from Lesson_13.models import ShipModel, PilotModel

URL = 'https://swapi.dev/api/starships'
SHIP_NAME = 'Millennium Falcon'

ships = requests.get(URL).json().get('results')
pilot_list = []
for ship in ships:
    if ship['name'] == SHIP_NAME:
        ship_falcone = ShipModel.from_dict(ship)
        for pilot_url in ship_falcone.pilots:

            pilot = PilotModel.from_dict(requests.get(pilot_url).json())
            pilot_list.append(pilot)

ship_falcone.pilots = pilot_list

pprint(ship_falcone.to_dict())
