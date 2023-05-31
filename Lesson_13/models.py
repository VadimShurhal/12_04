from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PilotModel:
    name: str
    height: str
    mass: int
    homeworld: str
    films: List[str]
    species: List[object]
    vehicles: List[object]
    starships: List[str]
    created: str
    edited: str
    url: str


@dataclass_json
@dataclass
class ShipModel:
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

