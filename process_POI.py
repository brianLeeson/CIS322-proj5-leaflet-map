def process():
	'''
	processes_POI.txt and returns a list of dicts containing the items
	'''
	poi_list = []
	
	with open('POI_trailheads.txt', 'r') as f:
		read_data = f.readlines()
	
	for line in read_data:
		parts = line.split(",")
		point_data = {"disc": parts[0].strip(), "lat": float(parts[1].strip()), "lon": float(parts[2].strip())}
		poi_list.append(point_data)
		
	return poi_list
	
print(process())
