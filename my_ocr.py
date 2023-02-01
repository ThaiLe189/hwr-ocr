import tensorflow as tf
import cv2


def _sort_rect(rect, cols):
    tolerance_factor = 10
    return ((rect["Y_min"] // tolerance_factor) * tolerance_factor) * cols + rect[
        "X_min"
    ]


def _predict_model(sess: object, img: object) -> object:
    # ghi ra file gray cho giống y đầu vào của aocr gốc
    matGray_OpenCV = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    success, encoded_image = cv2.imencode(".jpg", matGray_OpenCV)
    png_bytes = encoded_image.tobytes()
    input_feed = {}
    input_feed[
        "input_image_as_bytes:0"
    ] = png_bytes  # truyền vào chỗi bytes nén PNG, AOCR sé decode_png để trả lại ma trận ảnh
    input_feed["is_training:0"] = False
    output_feed = ["prediction:0", "probability:0"]

    outputs = sess.run(output_feed, input_feed)
    text = outputs[0]
    probability = outputs[1]
    text = text.decode("utf-8")

    # return (text, probability)
    return str(text), probability


def load_model_recog(init, meta, checkpoint):
    sess_init = tf.Session()
    tf.train.import_meta_graph(init)
    sess = sess_init
    saver = tf.train.import_meta_graph(meta)
    saver.restore(sess, tf.train.latest_checkpoint(checkpoint))
    return sess


def recognize_images(model, list_area, path_to_image):
    img = cv2.imread(path_to_image)
    text = ""
    list_area.sort(key=lambda x: _sort_rect(x, img.shape[1]))
    for area in list_area:
        img_crop = img[
                   int(area["Y_min"]): int(area["Y_max"]),
                   int(area["X_min"]): int(area["X_max"]),
                   ]
        color_covert = cv2.cvtColor(img_crop, cv2.COLOR_BGR2RGB)
        text_rec, _ = _predict_model(model, color_covert)

        text += text_rec + "\n"
    return text
