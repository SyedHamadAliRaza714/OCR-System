%%writefile app.py
from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from jiwer import wer, cer
import time

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def preprocess_image(image):
    img = np.array(image)
    h, w = img.shape[:2]
    if max(h, w) < 800:
        img = cv2.resize(img, None, fx=2, fy=2)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    return Image.fromarray(binary)

def get_confidence(image):
    data = pytesseract.image_to_data(
        image,
        lang="urd",
        config="--oem 1 --psm 6",
        output_type=pytesseract.Output.DICT
    )
    confs = []
    for conf in data["conf"]:
        try:
            conf = int(conf)
            if conf > 0:
                confs.append(conf)
        except:
            continue
    return sum(confs)/len(confs) if confs else 0

def extract_text(file_path):
    results = []
    pages = []
    if file_path.lower().endswith(".pdf"):
        images = convert_from_path(file_path, dpi=300)
        total_pages = len(images)
        for i, img in enumerate(images):
            processed = preprocess_image(img)
            text = pytesseract.image_to_string(
                processed, lang="urd", config="--oem 1 --psm 6"
            )
            confidence = get_confidence(processed)
            results.append({
                "page": i + 1,
                "text": text,
                "confidence": confidence
            })
            pages.append(round((i+1)/total_pages*100, 2))
            time.sleep(0.05) 
    else:
        img = Image.open(file_path)
        processed = preprocess_image(img)
        text = pytesseract.image_to_string(
            processed, lang="urd", config="--oem 1 --psm 6"
        )
        confidence = get_confidence(processed)
        results.append({"page": 1, "text": text, "confidence": confidence})
        pages.append(100)
    return results, pages

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file = request.files.get("file")
        if not file:
            return jsonify({"error": "No file uploaded."})

        truth = None

        if "ground_truth" in request.form:
            truth = request.form.get("ground_truth")

        elif "ground_truth_file" in request.files:
            gt_file = request.files.get("ground_truth_file")
            if gt_file and gt_file.filename.lower().endswith(".txt"):
                try:
                    truth = gt_file.read().decode("utf-8")
                except:
                    truth = None

        print("FILES RECEIVED:", request.files)

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        ocr_results, progress_list = extract_text(path)
        avg_conf = round(sum(r["confidence"] for r in ocr_results)/len(ocr_results), 2)

        wer_score = cer_score = None
        if truth:
            all_text = "\n".join([r["text"] for r in ocr_results])
            wer_score = round(wer(truth, all_text) * 100, 2)
            cer_score = round(cer(truth, all_text) * 100, 2)

        return jsonify({
            "file_name": file.filename,
            "results": ocr_results,
            "progress": progress_list,
            "avg_conf": avg_conf,
            "wer": wer_score,
            "cer": cer_score
        })

    return render_template("index.html")
