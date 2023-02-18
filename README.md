
# Railway Inspection System

The project helps in improvising the railway system using deep learning and video analytics. 
Implementation done are: 
- Object Detection using YOLOv5 (You Only Look Once)
- Speed Comparison between the train and the speed limit detected object 
- Track Fault Detection
- Adversarial Training using FGSM (Fast Gradient Sign Method)
- Video Analytics for VSS (Video Surveillance System)



## Demo

![video_gif](https://user-images.githubusercontent.com/59758501/219857516-b5688706-5934-4950-8174-b67aee88a59a.gif)

## LLD

[Documentation](https://docs.google.com/document/d/1gAiBFeojFVgkTZRK-76d5EVEV-5gINCB/edit?usp=sharing&ouid=102649797053030661895&rtpof=true&sd=true)


## Roadmap

1. Create the custom dataset.
2. Data Augmentation Techniques involved : using Keras ImageDataGenerator (that includes rotation_range, random rotation between 0 and 30, width_shift_range, height_shift_range, shear_range, zoom_range, horizontal_flip, brightness_range, fill_mode), Adding noise (Gaussian, Impulse, Uniform), Adding blurs (Gaussian, Averaging, Medium, Vertical and Horizontal)
3. Train the model for the class labels : road_crossing, barriers, catenary poles, main_signal, people, vehicles, speed_signal, and warning using YOLOv5 Algorithm.
4. Detect and crop the speed_signal objects.
5. Extract the speed limit from the speed_signal board using EasyOCR - Easy Optical Character Recognition.
6. Calculate the speed of the train using Cascading Techniques.
7. Compare the speed between the train and the detected speed limit nearby the train tracks.
8. Display the warnings




## Screenshots


![image](https://user-images.githubusercontent.com/59758501/219857664-307dc698-bf21-4912-a748-4c9bb885f70d.png)
![image](https://user-images.githubusercontent.com/59758501/219857843-c4a2e2c9-0c68-408a-ae4d-15c10d6f5e45.png)
![image](https://user-images.githubusercontent.com/59758501/219857684-5b10ca7f-cccd-48c6-baa1-e9a0c927d074.png)
![image](https://user-images.githubusercontent.com/59758501/219857708-ac7fb5c9-3ebb-44bb-b108-e988c5449ead.png)
![image](https://user-images.githubusercontent.com/59758501/219857698-3f6c8956-c6bb-418a-aaa1-67fbcc9b1b59.png)
![image](https://user-images.githubusercontent.com/59758501/219857605-be4f075f-193e-482c-85e8-430fe5b660fd.png)



## Used By

This project can be used by:

- Railway Maintenance Department
- RPF - Railway Protection Force
- Project Improvement Enthusiasts


## Future Improvements

- The project can be extended to perform various other options like controlling the hardware system when the speed of train is not up-to the par
- Build other types of adversarial attacks for more perturbed training for the model
- Using the Video Surveillance System, Face Recognition System and Object/Person tracking can be implemented to find if the specific person has crossed the region in the video.
