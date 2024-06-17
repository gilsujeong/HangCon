## Download the dataset

LINK to the dataset

## Dataset Description

# HangCon(Hanging Objects in Construction Sites) Dataset

1. Data Collection
- Collecting images from surveillance videos recorded in real construction sites in South Korea.
- Duration of Data Collection: 102 days to capture diverse backgrounds and seasonal changes.
- Camera Setup:
  * Total Cameras: 6 cameras(D1, D2, D3, D4, D8, S)
  * Long-range Camera: One camera positioned at a distance in a different building for a broad perspective.
  * Close-up Cameras: Five cameras installed closer to the action for detailed views.
  * Object Focus: diverse hanging objects varying in size and shape
  * Recording Schedule: Cameras recorded video during business hours, Monday to Friday from 7 AM to 5 PM; no recordings on holidays due to no construction activity.

- Total: 101,381 images(50,842 of hanging objects and 50,539 of non-hanging objects) 
- Datset split : Train-57,704, Val-6,457, Test-37,220
- Training + Validation Set: 
  - Total Images: 64,161 
    - Training: 57,704 
    - Validation: 6,457 
  - D1: Ranges from dates 22.12.01 to 23.03.02, and 230414 to 23.05.12
  - D2, D3, D4, D8, S: Ranges from dates 22.12.01 to 23.03.02
- Test Set:
  - Total Images: 37,220
  - D1: Not included in the test set
  - D2, D3, D4, D8: Ranges from dates 23.04.14 to 23.05.12
  - S: Ranges from dates 23.03.23 to 23.04.30

2. Data Preprocessing
- Extracting images at 30 sec intervals from the raw videos.
- From the videos comprising each day, about 1,000 images (5% of all extracted images) contain at least one hanging object.
- Initial resolution of images from cameras A, B, C, D, and F is 1920x1080; camera E captures at 1280x720.
- All images resized to 640x360 for processing consistency.

3. Data Annotation
- Extracted images manually annotated for three classes: hanging object, rope, and hanging object with rope
- “Hanging object” is defined as any types of objects suspended by ropes from cranes.
- “Rope” is defined that the rope attached to the crane and holding the hanging object, with bounding box marked from the connected part of the object to the hook.
- “Hanging object with rope” is defined as a separate class that includes both the hanging object and the rope, marked by bounding boxes around the edges of both classes. This annotation is performed after the initial annotation of the two classes using simple mathematical calculations.

- Annotation performed by 13 annotators using Darklabel, a labeling software.
- All classes are annotated with bounding box coordinates in YOLO format(.txt)(normalized x center, y center, width, height) and class labels.
- Annotations are converted into COCO(.json) and VOC(.xml) formats to ensure compatibility with various object detection frameworks.

4. Classes
  exp1: ["Hanging object"]
  exp2: ["Hanging object", "Rope"]
  exp3: ["Hanging object", "Rope", "Hanging object with rope"]       
