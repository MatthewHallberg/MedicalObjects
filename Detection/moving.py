import  send_message as message

max_boxes_to_draw = 20
min_score_thresh = .4
hold_filter = 0
empty_filter = 0
curr_message = 'm-empty'
last_message = 'm-empty'
is_holding = False
#HACK: hardcoded sizes
bottle_max = .03
syringe_max = .15

def check_moving(boxes,classes,scores,category_index):
	new_object_list = []
	#first load box object class and add each to list
	for i in range(min(max_boxes_to_draw, boxes.shape[0])):
	  	if scores is None or scores[i] > min_score_thresh:
	  		box = tuple(boxes[i].tolist())
	  		if classes[i] in category_index.keys():
	  			class_name = category_index[classes[i]]['name']
	  			name = str(class_name)
	  			length = box[3] - box[1]
	  			width = box[2] - box[0]
	  			sa = length * width
	  			#get_sizes(sa,name)
	  			check_for_holding_item(sa,name)

#use when setting up a new workspace
def get_sizes(sa,name):
	if (name == 'bottle'):
		print(sa)

def check_for_holding_item(sa,name):
	global is_holding
	global curr_message
	global last_message
	global hold_filter
	global empty_filter
	if (name == 'syringe' and sa > syringe_max):
		curr_message = 'holding: syringe'
		hold_filter += 1
		empty_filter = 0
	elif (name == 'bottle' and sa > bottle_max):
		curr_message = 'holding: bottle'
		hold_filter += 1
		empty_filter = 0
	else:
		curr_message = 'm-empty'
		empty_filter += 1
		hold_filter = 0
	#dont send duplicate messages
	if (last_message != curr_message):
		if (hold_filter > 3 or empty_filter > 3):
			if (hold_filter > 3):
				is_holding = True
			else:
				is_holding = False
			message.send_message(curr_message)
			last_message = curr_message


