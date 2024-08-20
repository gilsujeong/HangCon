===================
Related Code Description
===================

1. annotation_converter
- Annotation was performed by 13 annotators using Darklabel, a labeling software.
- All classes are annotated with bounding box coordinates in YOLO format (.txt) (normalized x center, y center, width, height) and class labels.
- Annotations were converted into COCO (.json) and VOC (.xml) formats to ensure compatibility with various object detection frameworks.

- Codes in this folder converts annotations from YOLO format (.txt) to COCO (.json) and VOC (.xml) formats.

2. Object Detection Packages
- As stated in the manuscript, to evaluate the quality and effectiveness of the proposed hanging object dataset "HangCon", experiments were conducted using representative benchmark object detection models.
- Total 10 models are selected and applied to the HangCon
- These models include Faster R-CNN, RetinaNet, Cascade R-CNN, CornerNet, CenterNet, DETR, ATSS, EfficientDet, Deformable-DETR, YOLOv5 and YOLOv8. 

- The mmdetection package was used for the detection evaluation of the HangCon dataset.
- YOLO was utilized with a separate package.

# Refer to the usage guide of each package due to different environment settings on each computer..

2-1. mmdetection
- MMDetection is an open source object detection toolbox based on PyTorch
- Used detection models with mmdetection: Faster R-CNN, RetinaNet, Cascade R-CNN, CornerNet, CenterNet, DETR, ATSS, EfficientDet, Deformable-DETR
- The COCO format annotations from HangCon were used for utilizing the mmdetection package.
- Github URL: https://github.com/open-mmlab/mmdetection
- Usage Guide: https://mmdetection.readthedocs.io/en/latest/get_started.html

2-2. yolo
- YOLO was utilized with a separate package, using two versions: v5 and v8.
- The YOLO format annotations from HangCon were used for utilizing the YOLO package.
1) yolov5
- Githus URL: https://github.com/ultralytics/yolov5

2) yolov8
- Github URL: https://github.com/ultralytics/ultralytics
- Usage Guide: https://docs.ultralytics.com/
- Train: train_HangCon.py
- Val: val_HangCon.py