
import json
import os
import sys
import time
import requests
from configuration import api
from utilities.distance import distance, km_to_ly
from classes.solar_system import SolarSystem
from services.solar_system import SolarSystemService
from typing import List
SOLAR_SYSTEMS: List[SolarSystem]= []

def load_system_info(offset = 0):

	with open("system_ids.json","r") as fp:
		d = json.load(fp)
		fullsize = len(d)
		d = d[offset:]
	print("Number of Entrie: ", len(d))
	os.system("mkdir system_info")
	count = offset
	for system_id in d:
		try:
			result = requests.get("{}universe/systems/{}/?datasource=tranquility&language=en-us".format(api, system_id)).json()
		except:
			print("Error with GET Request. 3 Sec Sleep, restarting.")
			time.sleep(3)
			load_system_info(count)
			return
		s: SolarSystem = SolarSystem.from_json(result)
		print("{} / {}: {}".format(count, fullsize, s.name) )
		with open("system_info/{}.json".format(s.name), "w") as fp:
			json.dump(result, fp)
		count += 1

def load_systems_into_memory():
	files = os.listdir("system_info")
	l = []
	for f in files:
		with open("system_info/{}".format(f), "r") as fp:
			l.append(SolarSystem.from_json(json.load(fp)))
	return l

def main():
	global SOLAR_SYSTEMS
	args = sys.argv[1:]
	if len(args) > 0 and args[0] == 'load':
		print("Fetching Systems.")
		load_system_info()
		exit()
	
	l = load_systems_into_memory()
	SOLAR_SYSTEMS = l
	if len(args) > 0 and args[0] == 'test':
		first_system = list(filter( lambda s: s.name.lower() == 'Jita'.lower(), l))
		first_system = first_system[0] if len(first_system) > 0 else None
		if first_system is None:
			print("First System Not Found.")
			return
		
		second_system = list(filter( lambda s: s.name.lower() == 'Hek'.lower(), l))
		second_system = second_system[0] if len(second_system) > 0 else None
		if second_system is None:
			print("Second System Not Found")
			return

		d = SolarSystemService.get_distance_ly_between_systems(first_system,second_system)
		print("Distance LY: ", d )

		print("Intersection of Systems between Samanuni and Y-4CFK")
		three = list(filter( lambda s: s.name.lower() == 'Samanuni'.lower(), l))
		three = three[0] if len(three) > 0 else None
		if three is None:
			print("Third System Not Found.")
			return

		four = list(filter( lambda s: s.name.lower() == 'Y-4CFK'.lower(), l))
		four = four[0] if len(four) > 0 else None
		if four is None:
			print("Fourth Not Found.")
			return

		iter_three = list(SolarSystemService.get_all_systems_within_range(SOLAR_SYSTEMS,three, 10))
		iter_four = list(SolarSystemService.get_all_systems_within_range(SOLAR_SYSTEMS,four, 10))
		intersection_systems = SolarSystemService.get_intersection_of_systems(iter_three, iter_four)
		info = [s.name for s in intersection_systems]
		print("Intersected Systems: ", info)
		print("Size of Intersection: ", len(info))
		print("Which Systems in Results has Stations? ", [s.name for s in intersection_systems if len(s.stations)>0])

	
if __name__ == "__main__":
	main()