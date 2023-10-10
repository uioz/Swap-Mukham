import os

FFMPEG_PATH = "./ffmpeg/ffmpeg" if os.path.exists("./ffmpeg/ffmpeg") else None

INSWAPPER_PATH = "./assets/pretrained_models/inswapper_128.onnx"
FACE_PARSER_PATH = "./assets/pretrained_models/faceparser.onnx"
ARCFACE_PATH = "./assets/pretrained_models/w600k_r50.onnx"
RETINAFACE_PATH = "./assets/pretrained_models/det_10g.onnx"
GENDERAGE_PATH = "./assets/pretrained_models/gender_age.onnx"

CODEFORMER_PATH = "./assets/pretrained_models/codeformer.onnx"
GFPGAN_V14_PATH = "./assets/pretrained_models/GFPGANv1.4.onnx"
GFPGAN_V13_PATH = "./assets/pretrained_models/GFPGANv1.3.onnx"
GFPGAN_V12_PATH = "./assets/pretrained_models/GFPGANv1.2.onnx"
GPEN_BFR_512_PATH = "./assets/pretrained_models/GPEN-BFR-512.onnx"
GPEN_BFR_256_PATH = "./assets/pretrained_models/GPEN-BFR-256.onnx"
RESTOREFORMER_PATH = "./assets/pretrained_models/restoreformer.onnx"