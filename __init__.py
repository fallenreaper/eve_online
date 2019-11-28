
import json
import os
import time
import requests
from configuration import api
from utilities.distance import distance, km_to_ly
from classes.system import SolarSystem
INIT = False

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
	offset = 3676
	if INIT:
		load_system_info(offset)
		return
	l = load_systems_into_memory()

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

	d = round(distance(first_system, second_system), 3)
	print("Distance KM:", d)
	print("Distance AU: ", km_to_ly(d) )

	
if __name__ == "__main__":
	main()