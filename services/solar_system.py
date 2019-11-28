
from classes.solar_system import SolarSystem
from utilities.distance import distance, km_to_ly
from typing import List, Iterator

class SolarSystemService:
    @staticmethod
    def get_distance_ly_between_systems(a: SolarSystem, b: SolarSystem, precision=3):
        return round(km_to_ly(distance(a,b)))

    @staticmethod
    def get_all_systems_within_range(list_of_systems: List[SolarSystem], a: SolarSystem, ly: float) -> Iterator[SolarSystem]:
        for s in list_of_systems:
            if km_to_ly(distance(a, s)) < ly:
                yield s

    @staticmethod
    def get_intersection_of_systems(a: List[SolarSystem], b: List[SolarSystem]) -> List[SolarSystem]:
        print("Lengths: ", len(a), len(b))
        d = { i.name: i for i in a}
        for s in b:
            d[s.name] = s
        temp = set([i.name for i in b]) 
        lst3 = [value for value in [i.name for i in a] if value in temp]

        return [d[name] for name in lst3] 
        