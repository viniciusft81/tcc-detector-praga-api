from ultralyticsplus import YOLO

def img_classification(image):
    # carrega modelo
    model = YOLO('foduucom/plant-leaf-detection-and-classification')

    # parâmetros do modelo
    model.overrides['conf'] = 0.25  # NMS confidence threshold
    model.overrides['iou'] = 0.45  # NMS IoU threshold
    model.overrides['agnostic_nms'] = False  # NMS class-agnostic
    model.overrides['max_det'] = 1000  # maximum number of detections per image

    # perform inference
    results = model.predict(image)
    print("=========================================")
    result = results[0]
    categories = result.boxes.cls
    print("category", categories)
    print("=========================================")
    
    if len(categories) > 0:
        if 5 in categories:
            return True
        else:
            return False
    else:
        return False
        