
from typing import List
class PlanetMetadata:
    def __init__(self):
        self.planet_id: int = -1
        self.moons: List[int] = []
        self.asteroid_belts: List[int] = []

    @classmethod
    def from_json(cls, js):
        item = cls()
        item.planet_id = js["planet_id"] if "planet_id" in js else -1
        item.moons = js["moons"] if "moons" in js else []
        item.asteroid_belts = js["asteroid_belts"] if "asteroid_belts" in js else []
        return item


class Planet:
    def __init__(self):
        pass