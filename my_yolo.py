import base64

import cv2
import torch

import my_env


def load_model(path_to_model):
    model = torch.hub.load(
        "ultralytics/yolov5", "custom", path=path_to_model, force_reload=True
    )
    return model


def _draw_rectangle(image, x1, y1, x2, y2):
    return cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 3)


def _call_yolo(model, path_to_image, path_save_output):
    results = model(path_to_image)
    img = cv2.imread(path_to_image)
    list_output = []
    output = {
        "Label": "",
        "X_min": 0,
        "Y_min": 0,
        "X_max": 0,
        "Y_max": 0,
    }
    for i in results.pandas().xyxy[0].values.tolist():
        # confidence
        if i[4] > 0.6:
            img = _draw_rectangle(img, i[0], i[1], i[2], i[3])
            output["Label"] = i[6]
            output["X_min"] = i[0]
            output["Y_min"] = i[1]
            output["X_max"] = i[2]
            output["Y_max"] = i[3]
            output_copy = output.copy()
            list_output.append(output_copy)
    cv2.imwrite(path_save_output, img)
    return img, list_output


def predict_model(model: str, path_to_input: str):
    path_save_output = my_env.OUTPUT_FOLDER + path_to_input.replace(
        my_env.UPLOAD_FOLDER, ""
    )
    img, list_output = _call_yolo(model, path_to_input, path_save_output)
    # image to base64
    _, im_arr = cv2.imencode(".jpg", img)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64, list_output
