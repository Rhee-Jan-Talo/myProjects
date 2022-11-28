import cv2

#pic1 = cv2.imread("fruits.jpg")
cap = cv2.VideoCapture(0)

class_name = []
classFile = 'coco.names'

thres = 0.45

with open(classFile,'rt') as f:
       class_name=f.read().rstrip('\n').split('\n')

configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)


temp = True
while temp == True:
       success, img = cap.read()
       classIds, confs, bbox = net.detect(img, confThreshold = thres)

       if len(classIds) != 0:
              for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                     cv2.rectangle(img, box, color=(0,255,0), thickness = 2)
                     cv2.putText(img, class_name[classId-1].upper(), (box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                     cv2.putText(img, str(round(confidence*100))+'%', (box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

       cv2.imshow("Output", img)
       cv2.waitKey(1)
