import  send_message as message

max_boxes_to_draw = 20
min_score_thresh=.2
curr_message = 'none'
last_message = 'none'

class boxObject:
	xMin = 0
	xMax = 0
	yMax = 0
	name = ''