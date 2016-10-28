def process():
	'''
	processes_POI.txt and return a list of dicts containing the points lat, long and discription
	poi_list = [{'lat': lat#, 'lon': lon#, 'disc': 'text'}, {...}, ...]
	'''
	poi_list = []
	
	with open('POI_trailheads.txt', 'r') as f:
		read_data = f.readlines()
	
	for line in read_data:
		parts = line.split(",")
		point_data = {"lat": float(parts[1].strip()), "lon": float(parts[2].strip()), "disc": parts[0].strip()}
		poi_list.append(point_data)
		
	return poi_list