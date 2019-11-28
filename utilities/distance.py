
from classes.solar_system import SolarSystem
import math
def distance(a: SolarSystem, b: SolarSystem) -> int:
    """Return KM"""
    # r**2 = a**2 + b**2 + c**2
    # dist between 2:
    #  r = sqrt((ax-bx)**2 + (ay-by)**2 + (az-bz)**2)
    return math.ceil(
        math.sqrt(
            math.pow(a.position.x - b.position.x, 2) + 
            math.pow(a.position.y - b.position.y, 2) + 
            math.pow(a.position.z - b.position.z, 2)
            )
    ) / 1000

def km_to_au(km: int) -> int:
    return km / 149598000

def au_to_ly(au: int) -> int:
    return au / 63018.867925

def km_to_ly(km: int) -> int:
    return au_to_ly(km_to_au(km))
