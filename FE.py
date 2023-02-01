import streamlit as st

from PIL import Image
from io import BytesIO
import base64
import requests

import json

st.set_page_config(layout="wide", page_title="Thái OCR")

st.write("## Nhận dạng chữ viết tay")

st.sidebar.write("## Tải hình ảnh cần nhận dạng :gear:")
API_ENDPOINT = "http://localhost:5000/cvt"


def call_api(imageBase64):
    payload = json.dumps({"ImageBase64": str(imageBase64)})
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "POST", API_ENDPOINT, headers=headers, data=payload)
    data = response.json()
    return data

# Download the fixed image


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fill_text(text):
    col3.write("Kết quả nhận dạng")
    col3.text(text)


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Ảnh ban đầu")
    col1.image(image)

    im_bytes = convert_image(image)
    res = call_api(
        (base64.b64encode(im_bytes)).decode("utf-8"))
    
    fixed = res["url_image"]
    col2.write("Ảnh sau khi detect")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    fill_text( res["text"])


col1, col2, col3 = st.columns(3)

my_upload = st.sidebar.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
