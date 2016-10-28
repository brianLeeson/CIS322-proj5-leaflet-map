#NOSETESTS
#tests file processing function

import POI_process

def test_process():
	d_struct = POI_process.process()
	assert (d_struct[0]['lat'] == 44.03229)
	assert (d_struct[1]['lon'] == -123.08076)
	assert (d_struct[2]['disc'] == "Ridgeline Foxhollow")
