# Human-Fall-Detection-Using-ML

## Introduction :
As our world undergoes a significant shift in its population dynamics, the number of individuals aged 65 and above reached a staggering 771 million in 2022, constituting almost 10% of the global population. This societal transition is not merely a statistical observation; it represents a profound change. With expectations pointing to a rise to 16% by 2050 and a striking 24% by the year 2100, the aging population poses unique challenges. One such challenge is the increasing concern for fall-related incidents among the elderly, making it imperative to implement effective fall detection mechanisms.

In the exploration of fall detection mechanisms, various approaches have been experimented with and tested. Certain approaches utilize sensors, specifically wearable sensors designed to detect falls. These sensors employ a quaternion algorithm to transmit requests for assistance and the person's location to caregivers. This algorithm is applied to acceleration data. However, this method runs the risk of
generating false alarms, as it may incorrectly interpret instances of sleeping or lying down as falls. Others utilize RGBD (Red, Green, Blue, Depth) videos to extract features. Additionally, some models combine both sensor and camera-based mechanisms, extracting features from camera captures and sensor information synergistically to enhance overall detection accuracy. Review of these methods along with some others have been mentioned in this literature review. In our study, our primary focus lies on evaluating the accuracy of fall detection using RGB videos on URFD dataset. Extracting the key joints from 11-32 excluding the facial joints as they won’t play a role in identifying instances of falling. These key joints are then used to calculate the inter point distances between each other. The feature vector for all the frames in the video sequence is calculated and given to machine learning model for testing and training, finally the average of accuracy is depicted using leave-one-out Strategy for various models. The leave-one-out strategy is depicted in here, the same dataset we used (URFD) was used there for fall detection.

![image](https://github.com/MdSaifurRahman/Human-Fall-Detection-Using-ML/assets/100013081/911dfaeb-fae7-4c2c-aa07-f648d60d748f)


## Data Preprocessing :
We utilized the URFD (U R Fall detection) dataset comprising 30 fall sequences and 40 non-fall sequences.
Employed OpenCV for the video sequence, in this dataset the video sequences are available as set of frames (images). Also, it is used for converting frames to RGB format, and preprocessing.

● Utilized the Mediapipe library for human pose estimation, allowing the detection of joint positions in each frame.

● Mediapipe Pose operates with images in the RGB (Red, Green, Blue) format, whereas OpenCV, as the default, reads video files in the BGR (Blue, Green, Red) format.

● To utilize Mediapipe Pose effectively, it is necessary to convert the input video frames from BGR to RGB. This conversion can be achieved using the cvtColor() function from OpenCV, employing the COLOR_BGR2RGB flag.

● This transformation swaps the red and blue channels, ensuring compatibility between the images and Mediapipe Pose.

### Detecting the landmarks:
● Mediapipe Pose is employed to identify landmarks, which represent joint positions on the human body within every frame.

● These landmarks correspond to distinct points on the body, including shoulders, elbows, wrists, hips, knees, and ankles.

● In case of fall event, the relative position of facial landmarks does not change, so they are unnecessary to be included in.

● Hence for this project, the face landmarks (joint IDs 0 to 10) are disregarded.3
![image](https://github.com/MdSaifurRahman/Human-Fall-Detection-Using-ML/assets/100013081/494e4a97-61c2-4cd9-b8df-4bcd7e2505df)


### Joint Extraction:
● Implemented a joint extraction approach using a combination of OpenCV and Mediapipe libraries.

● OpenCV handled general image and video processing tasks.

● Mediapipe was employed for human pose estimation, detecting joint positions accurately.

● When applied directly, handling the information complexity of a 3-D figure can pose a significant challenge and may not be easily processed.

● So, the joints will be of x-y coordinates and model will be employing simply on 2-D figure rather than processing 3-D figure directly.45


### Frame Selection:
Considered the first n frames from each sequence, where n is the number of frames in the sequence with the minimum number of frames. This step ensuredconsistency in the analysis across different sequences.

### Feature Matrix Construction:
● Constructed a 2D feature matrix for every frame in all sequences.

● Calculate the distance between all pairs of joints for each frame. Using the Euclidean distance formula, Distance = (sqrt (x2 - x1) ^2 + (y2 - y1) ^2), to compute the distance between two joints (x1, y1) and (x2, y2).

● Generate a matrix as the output, where each element signifies the distance between two joints in a specific frame.

● The feature vectors served as inputs for subsequent machine learning models

● Similarly, as above, we also Constructed a 2D feature matrix for every frame in all sequences, but for coordinates.

● The raw coordinates extracted from MediaPipe are directly arranged in the format of [(x1, y1) (x2, y2) …., (xn, yn)]

● Generate a matrix as the output, where each element signifies the coordinate of the figure from which the joint data is extracted.

● This feature vector too served as inputs for subsequent machine learning models.


### Feature Vector:
● The feature matrix is converted into a 1D array known as a feature vector.

● This transformation is done by concatenating the rows of the matrix into a single vector.

● The first feature vector contains distances between all pairs of joints in each frame contained in all fall and non-fall sequences in a sequential manner.

● The second feature vector which was used consists of raw coordinates arranged in 1-D similar to the distance vector.

## ML Model Input Phase:
● Applied five distinct machine learning models for classification:
⮚ Decision Tree Classifier
⮚ Linear Support Vector Machine (SVM)
⮚ Logistic Regression
⮚ Voting based model
⮚ Random forest generator

● Used the 2D feature vector and coordinate feature vector as input to these models for the classification of fall/non-fall to each sequence.

### Validation Strategy:
● Implemented the leave-one-out validation strategy.

● In a leave-one-out cross-validation approach, each data point (or video sequence in your case) is used as the test set exactly once, while the rest of the data is used for training. This process is then repeated for each data point in the dataset.

● Leaving one example out at a time for testing ensures that the model is evaluated on as much diverse data as possible, given the limited amount of information available.

### Performance Evaluation:
● Evaluated the performance of each model using accuracy as a metric.

● Compared the results across the five models to identify the most effective approach for fall detection.

● A consistently performing model can provide insight into which model is better suited for fall detection.

## Conclusion
In summary, the fall detection study explored two distinct feature representations—distances between joints and X, Y coordinates of joints—evaluating the performance of various machine learning models.

● Logistic Regression consistently emerged as a top-performing model, achieving the highest accuracies in both scenarios (91.42% with joint distances and 88.57% with coordinates).

● The Support Vector Machine (SVM) exhibited competitive accuracy, achieving 88.57% with distances and 84.28% with coordinates. 

● The Random Forest Classifier demonstrated exceptional performance, surpassing other models with 92.85% accuracy using joint distances and an even higher 95.71% with coordinates.

● These findings highlight the nuanced nature of fall detection methodologies, emphasizing the importance of model selection and feature representation in achieving accurate and reliable results.

● The outcomes provide valuable insights for future research endeavours, paving the way for the development of more effective and versatile fall detection systems.


