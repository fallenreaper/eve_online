
from ..classes.system import SolarSystem
from ..utilities.distance import distance, km_to_ly

class SolarSystemService:
    @staticmethod
    def get_distance_ly_between_systems(a: SolarSystem, b: SolarSystem, precision=3):
        return round(km_to_ly(distance(a,b)))