
from typing import List
from .planet import PlanetMetadata
from .position import Position

class SolarSystem:

	def __init__(self):
		self.constellation_id: int = -1
		self.name: str = ""
		self.planets: List[PlanetMetadata] = []
		self.position: Position = Position()
		self.security_status: float = None
		self.star_id: int = -1
		self.stargates: List[int] = []
		self.stations: List = []
		self.system_id: int = -1
	
	@classmethod
	def from_json(cls, js):
		item = cls()
		item.constellation_id = js["constellation_id"] if "constellation_id" in js else -1
		item.name = js["name"] if "name" in js else ""
		_p = js["planets"] if "planets" in js else []
		item.planets = [ PlanetMetadata.from_json(p) for p in _p]
		item.position = Position.from_json(js["position"]  if "position" in js else {})
		item.security_status = js["security_status"] if "security_status" in js else None
		item.star_id = js["star_id"] if "star_id" in js else -1
		item.stargates = js["stargates"] if "stargates" in js else []
		item.stations = js["stations"] if "stations" in js else []
		item.system_id = js["system_id"] if "system_id" in js else -1
		return item
