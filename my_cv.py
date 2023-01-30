import cv2

import my_ocr
import my_yolo


def handle_ocr_cv(list_area: list, path_image: str, model_detect_ci: str, model_rec: str) -> list:
    img = cv2.imread(path_image)
    res = {
        "Label": "",
        "Text": ""
    }
    list_res = []
    for area in list_area:
        # new path area drop
        path_new = path_image.replace(".jpg", "_" + area["Label"] + ".jpg")
        # crop image and save image
        crop_img = img[
                   int(area["Y_min"]): int(area["Y_max"]),
                   int(area["X_min"]): int(area["X_max"]),
                   ]
        cv2.imwrite(path_new, crop_img)

        # Rec area CV
        _, area_yolo = my_yolo.predict_model(model_detect_ci, path_new)

        if len(area) != 0:
            text = my_ocr.recognize_images(model_rec, area_yolo, path_new)
        else:
            text = ""
        res["Label"] = area["Label"]
        res["Text"] = text
        output_copy = res.copy()
        list_res.append(output_copy)

    return list_res
