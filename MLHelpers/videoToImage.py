import cv2

#this script should ouput about 100 images for a 25 second iPhone video
pathToVideoFile = 'Videos/bottle.mp4'
outputFolder = 'BottleImages'#make sure to create this empty folder so the images have somewhere to go

vidcap = cv2.VideoCapture(pathToVideoFile)
success,image = vidcap.read()
count = 0
fileNum = 150 #start at different number for new video eg. 150 so images dont get overwritten
success = True
while success:
  success,image = vidcap.read()
  if count % 7 == 0:
  	fileNum += 1
  	cv2.imwrite(outputFolder + "/frame%d.jpg" % fileNum, image)# save frame as JPEG file      
  	print('Read a image: ', success)
  count += 1