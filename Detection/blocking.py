import  send_message as message
import moving

class boxObject:
	xMin = 0
	xMax = 0
	yMax = 0
	name = ''

max_boxes_to_draw = 20
min_score_thresh = .2
curr_message = 'b-empty'
last_message = 'b-empty'
empty_filter = 0

def check_blocking(boxes,classes,scores,category_index):
	global curr_message
	global last_message
	global empty_filter
	objectList = []
	#first load box object class and add each to list
	for i in range(min(max_boxes_to_draw, boxes.shape[0])):
	  	if scores is None or scores[i] > min_score_thresh:
	  		box = tuple(boxes[i].tolist())
	  		if classes[i] in category_index.keys():
	  			class_name = category_index[classes[i]]['name']
	  			display_str = str(class_name)
	  			newBox = boxObject()
	  			newBox.xMin = box[1]
	  			newBox.xMax = box[3]
	  			newBox.yMax = box[2]
	  			newBox.name = class_name
	  			objectList.append(newBox)
	#loop through the list of current objects and check for blocking
	for i in range(len(objectList)):
		foundBlock = False
		for x in range(len(objectList)):
			if (objectList[i].xMin > objectList[x].xMin and objectList[i].xMin < objectList[x].xMax):
				if (objectList[i].yMax > objectList[x].yMax):
					curr_message = objectList[i].name + ' blocking airflow to ' + objectList[x].name
					empty_filter = 0
				else:
					curr_message = objectList[x].name + ' blocking airflow to ' + objectList[i].name
					empty_filter = 0
				foundBlock = True
				break
		if (foundBlock == False):
			empty_filter += 1
			if(empty_filter > 3):
				curr_message = 'b-empty'
	#if we are holding an object send a message that we arent blocking 
	if (moving.is_holding == True):
		curr_message = 'b-empty'
	if (curr_message != last_message):
		message.send_message(curr_message)
		last_message = curr_message

