def process():
	'''
	processes_POI.txt and returns a list of tuples containing the items
	'''
	poi_data = []
	
	with open('POI_trailheads.txt', 'r') as f:
		read_data = f.readlines()
	
	for line ine read_data:
		point = (line[0], line[1], line[2])
		poi_data.append(point)
	
	return poi_data