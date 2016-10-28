#NOSETESTS
#tests file processing function

import process_POI

def test_process():
	d_struct = process_POI.process()
	assert (d_struct[0]['lat'] == 44.03229)
	assert (d_struct[1]['lon'] == -123.08076)
	assert (d_struct[2]['disc'] == "Ridgeline Foxhollow")
