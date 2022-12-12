# Railway_Inspection_System

yolo_final_video.ipynb


This file compares and warns the system if the speed of train exceeds the limit detected nearby in the speed signal board limit that is found using YOLOv5 algorithm and EasyOCR model. The model is pre-trained with 500 epochs.

dataaugmentation.ipynb


The file augments multiple images by adding different types of noises, blurrs and other augmentation techniques.

preprocessing.ipynb


The file preprocesses the images that are detected using Object Detection Algorithm and Optical Character Recognition Model.

track_fault_detection.py


The is file contains ResNet Algorithm using resnet.ipynb, to detect if there is any fault in the train track image provided and sends SMS message to the provided number regarding the fault in the train track image. The number provided is the track maintenance team number. 

fgsm perturbations.ipynb


The file trains the model for adversarial attack using Fast Gradient Sign Method which is a white box testing whose goal is to train the model during misclassification by adding perturbations with epsilon values.

Person_Counter_final


This folder contains the video analytics that counts the number of people in the given frame at once.

