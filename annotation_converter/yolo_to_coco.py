import os
import json
import numpy as np
from tqdm import tqdm
from PIL import Image

'''
images: file_name, height, width, id
categories: supercategory, id, name
annotations: id, image_id, bbox, area, iscrowd, category_id, (segmentation제외)
'''

# Define paths
data_dir = './dataset'
coco_annotation_dir = './dataset'

# Create COCO annotation directory if it doesn't exist
if not os.path.exists(coco_annotation_dir):
    os.makedirs(coco_annotation_dir)

# COCO categories
coco_categories = [
    {"supercategory": "object", "id": 0, "name": "hanging_object"}
]

# Function to convert YOLO bbox to COCO bbox
def yolo_to_coco_bbox(yolo_bbox, img_width, img_height):
    x_center, y_center, bbox_width, bbox_height = yolo_bbox
    x_min = max(0, (x_center - bbox_width / 2) * img_width)
    y_min = max(0, (y_center - bbox_height / 2) * img_height)
    x_max = min(img_width, (x_center + bbox_width / 2) * img_width)
    y_max = min(img_height, (y_center + bbox_height / 2) * img_height)
    return [x_min, y_min, x_max - x_min, y_max - y_min]

# Process train, test, and val sets
for split in ["train", "test", 'val']:
    yolo_labels_dir = os.path.join(data_dir, split, 'labels_wor')
    image_dir = os.path.join(data_dir, split, 'images')
    coco_annotation_file = os.path.join(coco_annotation_dir, f'coco_{split}_wor.json')

    # Initialize COCO annotations
    coco_annotations = {
        "images": [],
        "categories": coco_categories,
        "annotations": []
    }

    image_id_counter = 0
    annotation_id_counter = 0

    for filename in tqdm(os.listdir(yolo_labels_dir)):
        if filename.lower().endswith('.txt'):
            image_filename = os.path.splitext(filename)[0] + '.png'
            image_path = os.path.join(image_dir, image_filename)
            image = Image.open(image_path)
            img_width, img_height = image.size

            image_info = {
                "file_name": image_filename,
                "height": img_height,
                "width": img_width,
                "id": image_id_counter
            }
            coco_annotations["images"].append(image_info)

            with open(os.path.join(yolo_labels_dir, filename), 'r') as f:
                for line in f:
                    class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.strip().split())
                    coco_bbox = yolo_to_coco_bbox([x_center, y_center, bbox_width, bbox_height], img_width, img_height)
                    annotation = {
                        "id": annotation_id_counter,
                        "image_id": image_id_counter,
                        "bbox": coco_bbox,
                        "category_id": int(class_id),
                        "area": coco_bbox[2] * coco_bbox[3],
                        "iscrowd": 0
                    }
                    coco_annotations["annotations"].append(annotation)
                    annotation_id_counter += 1

            image_id_counter += 1

    # Save the COCO annotations
    with open(coco_annotation_file, "w") as f:
        json.dump(coco_annotations, f, indent=4)
