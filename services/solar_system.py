
from classes.solar_system import SolarSystem
from utilities.distance import distance, km_to_ly
from typing import List, Iterator

class SolarSystemService:
    @staticmethod
    def get_distance_ly_between_systems(a: SolarSystem, b: SolarSystem, precision=None):

        return round(km_to_ly(distance(a,b)), precision) if precision is not None else km_to_ly(distance(a,b))

    @staticmethod
    def get_all_systems_within_range(list_of_systems: List[SolarSystem], a: SolarSystem, ly: float) -> Iterator[SolarSystem]:
        for s in list_of_systems:
            if km_to_ly(distance(a, s)) <= ly:
                yield s

    @staticmethod
    def get_intersection_of_systems(a: List[SolarSystem], b: List[SolarSystem]) -> List[SolarSystem]:
        print("Lengths: ", len(a), len(b))
        d = { i.system_id: i for i in a }
        for s in b:
            d[s.system_id] = s
        temp = set([i.system_id for i in b]) 
        lst3 = [value for value in [i.system_id for i in a] if value in temp]

        return [d[system_id] for system_id in lst3] 
        