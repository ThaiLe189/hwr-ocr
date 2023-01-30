import os

# model detect resume
PATH_TO_MODEL_DETECT_CV = os.getenv(
    "PATH_TO_MODEL_DETECT_CV", "weights/detect_cv/best.pt"
)
# model Chu in
PATH_TO_MODEL_DETECT_CI = os.getenv(
    "PATH_TO_MODEL_DETECT_CI", "weights/detect_ci/best.pt"
)
PATH_TO_MODEL_REC_CI = os.getenv("PATH_TO_MODEL_REC_CI", "weights/recognize_ci/")
PATH_TO_MODEL_REC_CHECKPOINT_CI = os.getenv(
    "PATH_TO_MODEL_REC_CHECKPOINT_CI", "weights/recognize_ci/checkpoints"
)

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
