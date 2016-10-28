def process():
	'''
	processes_POI.txt and returns a list of dicts containing the items
	'''
	poi_list = []
	
	with open('POI_trailheads.txt', 'r') as f:
		read_data = f.readlines()
	
	for line in read_data:
		parts = line.split(",")
		point_data = {"disc": parts[0], "lat": parts[1], "lon": parts[2]}
		poi_list.append(point_data)
		
	return poi_list