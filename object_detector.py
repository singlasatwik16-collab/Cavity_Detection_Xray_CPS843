from flask import Flask, request, jsonify
from PIL import Image
import requests
import io
import base64
import os

app = Flask(__name__)

# ----------------------
# CONFIGURATION
# ----------------------
ROBOFLOW_API_KEY = "GX7lwRJk06bwvEEqxXTM" 
PROJECT_ID = "dentex-3xe7e"
MODEL_VERSION = "2"

ROBOFLOW_URL = f"https://detect.roboflow.com/{PROJECT_ID}/{MODEL_VERSION}?api_key={ROBOFLOW_API_KEY}"

ALLOWED_CLASSES = ["caries", "deep caries"] 

@app.route("/")
def root():
    return open("templates/index.html").read()

@app.route("/cavities")
def cavities_page():
    return open("templates/cavities.html").read()

@app.route("/cavity-view")
def cavity_view():
    return open("templates/cavity_view.html").read()

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["image_file"]
    return jsonify(run_inference(file))

def run_inference(file):
    img = Image.open(file.stream).convert("RGB")

    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    jpeg_bytes = buf.getvalue()

    # Send to Roboflow API
    response = requests.post(
        ROBOFLOW_URL,
        files={"file": ("image.jpg", jpeg_bytes, "image/jpeg")},
    )

    result = response.json()
    print("\n\n RAW ROBOFLOW RESPONSE")
    print(result)
    print("=================================\n\n")

    output = []

    if "predictions" not in result:
        return output

    for pred in result["predictions"]:
        class_name = pred["class"].lower()

        # Filter only caries + deep caries
        if class_name not in ALLOWED_CLASSES:
            continue

        x = pred["x"]
        y = pred["y"]
        w = pred["width"]
        h = pred["height"]

        x1 = int(x - w / 2)
        y1 = int(y - h / 2)
        x2 = int(x + w / 2)
        y2 = int(y + h / 2)

        prob = pred["confidence"]

        # -------------------------
        # Severity Logic
        # -------------------------
        if prob >= 0.75:
            severity = "High"
            color = "#FF3B30"  # red
        elif prob >= 0.50:
            severity = "Medium"
            color = "#FFCC00"  # yellow
        else:
            severity = "Low"
            color = "#34C759"  # green

        output.append({
            "bbox": [x1, y1, x2, y2],
            "severity": severity,
            "label": f"{severity} {class_name.title()} ({prob*100:.0f}%)",
            "probability": round(prob, 2),
            "color": color
        })

    return output


# ----------------------
# RUN APP
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
