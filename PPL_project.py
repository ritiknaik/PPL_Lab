import cv2
import numpy as np

# reading the weights and cfg files
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# reading the coco data set
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

# capturing from webcam
cap = cv2.VideoCapture(0)
# img = cv2.imread('image.jpg') 

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    # making blob from image
    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)

    # taking unconnected layer names and forward pass
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    # for displaying bounding boxes
    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                centre_x = int(detection[0] * width)
                centre_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(centre_x - w / 2)
                y = int(centre_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    # Non maximum supressions to display only one class
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # appearance of bounding box
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes)!=0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (0, 0, 0), 2)

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
