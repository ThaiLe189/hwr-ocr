import os

# model Chu viet tay
PATH_TO_MODEL_DETECT_CVT = os.getenv(
    "PATH_TO_MODEL_DETECT_CVT", "weights/detect_cvt/best.pt"
)
PATH_TO_MODEL_REC_CVT = os.getenv("PATH_TO_MODEL_REC_CVT", "weights/recognize_cvt/")
PATH_TO_MODEL_REC_CHECKPOINT_CVT = os.getenv(
    "PATH_TO_MODEL_REC_CHECKPOINT_CVT", "weights/recognize_cvt/checkpoints"
)

# system
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "input")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "output")
LOG = os.getenv("LOG", "log/LOG")
