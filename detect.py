def detect(model_path: str, image_path: str):
    model_yolo = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    results = model_yolo(image_path)
    res = results.pandas().xyxy[0]
    res['x0'] = (res['xmin'] + res['xmax'])//2
    res['y0'] = (res['ymin'] + res['ymax'])//2
    return res
