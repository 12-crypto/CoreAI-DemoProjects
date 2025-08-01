import os
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
import json
import matplotlib.pyplot as plt

LABELS = {
    'background': 0,
    'abstract': 1, 'author': 2, 'caption': 3, 'date': 4, 'equation': 5,
    'figure': 6, 'footer': 7, 'list': 8, 'paragraph': 9, 'reference': 10,
    'section': 11, 'table': 12, 'title': 13
}

def parse_docbank_file(txt_file):
    annotations = []
    
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            parts = line.strip().split('\t')
            if len(parts) < 10:
                continue
            
            try:
                token = parts[0]
                x0, y0, x1, y1 = map(float, parts[1:5])  
                label = parts[9]
                
                annotations.append({
                    'token': token,
                    'bbox': [x0, y0, x1, y1],
                    'label': label
                })
            except Exception as e:
                print(f"Error parsing line {line_num}: {e}")
    
    return annotations

def create_pixel_mask(annotations, image_width, image_height):
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    
    for ann in annotations:
        x0, y0, x1, y1 = ann['bbox']
        label = ann['label']
        label_id = LABELS.get(label, LABELS['paragraph'])  
        
        x0 = int(x0 * image_width / 1000.0)
        y0 = int(y0 * image_height / 1000.0)
        x1 = int(x1 * image_width / 1000.0)
        y1 = int(y1 * image_height / 1000.0)
        
        y0_flipped = image_height - y1
        y1_flipped = image_height - y0
        
        x0 = max(0, min(x0, image_width - 1))
        y0 = max(0, min(y0_flipped, image_height - 1))
        x1 = max(0, min(x1, image_width - 1))
        y1 = max(0, min(y1_flipped, image_height - 1))

        if x1 > x0 and y1 > y0:
            mask[y0:y1, x0:x1] = label_id
        else:
            print(f"Skipped invalid box: {x0},{y0} -> {x1},{y1}")
            pass
    mask = np.flipud(mask)
    return mask

def convert_docbank_samples(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    (output_path / "images").mkdir(parents=True, exist_ok=True)
    (output_path / "masks").mkdir(parents=True, exist_ok=True)
    
    converted = 0

    for txt_file in input_path.glob("*.txt"):
        print(f"Processing: {txt_file.name}")
        
        prefix = txt_file.stem
        image_file = None
        for ext in ['_ori.jpg', '.jpg', '.png']:
            potential_image = input_path / f"{prefix}{ext}"
            if potential_image.exists():
                image_file = potential_image
                break
        
        if not image_file:
            print(f"No image found for {txt_file.name}")
            continue
        
        annotations = parse_docbank_file(txt_file)
        if not annotations:
            print(f"No valid annotations found in {txt_file.name}")
            continue
        
        try:
            image = Image.open(image_file)
            width, height = image.size
            print(f"Image size: {width}x{height}")
        except Exception as e:
            print(f"Could not load image {image_file.name}: {e}")
            continue
        
        mask = create_pixel_mask(annotations, width, height)
        
        output_image = output_path / "images" / f"{prefix}.jpg"
        output_mask = output_path / "masks" / f"{prefix}_mask.png"
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(output_image, quality=95)
        
        Image.fromarray(mask, mode='L').save(output_mask)
        
        print(f"Converted {len(annotations)} annotations to {width}x{height} mask")
        converted += 1
    
    print(f"Converted {converted} samples successfully!")
    print(f"Images saved to: {output_path / 'images'}")
    print(f"Masks saved to: {output_path / 'masks'}")
    
    with open(output_path / "labels.json", 'w') as f:
        json.dump(LABELS, f, indent=2)
    
    print(f"Label mapping saved to: {output_path / 'labels.json'}")
    
    return converted

if __name__ == "__main__":
    input_dir = "DocBank/DocBank_samples/DocBank_samples"  
    output_dir = "pixel_segmentation_dataset"              
    
    print("Converting DocBank samples to pixel segmentation format...")
    converted = convert_docbank_samples(input_dir, output_dir)
    
    if converted > 0:
        print(f"Dataset ready for training!")
    else:
        print("No samples converted. Check input directory and file formats.")