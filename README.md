📌 AI-Powered Dental Cavity Detection System
CPS843 – Computer Vision Project

🎥 Demo Video

Click below to watch the full project demo video:
[**Demo Video (GitHub Release)**](https://github.com/singlasatwik16-collab/Cavity_Detection_Xray_CPS843/releases/tag/Demo_Video)

🧠 Overview

This project is an AI-based dental X-ray analysis system that detects:
🦷 Caries
🦷 Deep Caries

It uses a Roboflow YOLOv8 model (Dentex v2) and a fully custom-built Flask backend + HTML/JS front-end interface.
The system provides:

✔ Real-time cavity detection
✔ Bounding-box visualization
✔ Severity scoring (High / Medium / Low)
✔ A dedicated Cavity Viewer with HD sharpening
✔ A full-screen, futuristic UI with video background
✔ Local persistence to view cavities individually

This project demonstrates computer vision, image processing, UI/UX, backend integration, and applied machine learning.

🚀 Features
🔍 1. AI Detection

Uses Roboflow Dentex v2 model

Detects only:
caries
deep caries
Confidence threshold-based severity classification
JSON output for bounding boxes, confidence, labels

🖥 2. Beautiful Web Interface

Video background
Neon-themed medical UI
Animated transitions
Clear upload → analyze → results workflow

🖼 3. Results Summary

Total cavities
Count by severity
Average confidence
Highest confidence
Risk level (Low / Moderate / High)

🔎 4. Cavity Viewer (HD)

Each cavity can be viewed individually:
High-resolution crop
Automatic upscaling
Sharpening using convolution kernel
Improved visibility for analysis
Navigation between cavities
Bounding box overlay

🧰 Tech Stack
Backend
Python
Flask
Roboflow Inference API
Pillow
Frontend
HTML5
CSS3 (Neon UI)
JavaScript (custom logic, canvas drawing)
LocalStorage state management

Canvas sharpening + resizing

📂 Folder Structure
Cavity_Detection_Xray_CPS843/
│
├── object_detector.py                  # Main Flask backend
├── templates/
│   ├── index.html          # Upload + analysis UI
│   ├── cavities.html       # Cavity list page
│   ├── cavity_view.html    # HD zoom viewer
│
├── static/
│   ├── images/logo.png
│   ├── videos/background.mp4
│   ├── css, js (embedded)
│
└── best.pt
└── dental images
└── README.md

🧪 How Detection Works
1️⃣ User uploads dental X-ray
2️⃣ Flask sends image → Roboflow API
ROBOFLOW_URL = f"https://detect.roboflow.com/{PROJECT_ID}/{MODEL_VERSION}?api_key={ROBOFLOW_API_KEY}"
3️⃣ Model returns:
Bounding boxes
Class (caries / deep caries)
Confidence
4️⃣ We apply severity rules:
if prob >= 0.75: severity = "High"
elif prob >= 0.50: severity = "Medium"
else: severity = "Low"
5️⃣ Frontend draws boxes + labels on canvas
6️⃣ Cavity Viewer extracts and sharpens the crop

🛠 Local Setup
1. Clone Repo
git clone https://github.com/singlasatwik16-collab/Cavity_Detection_Xray_CPS843.git
cd Cavity_Detection_Xray_CPS843

2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run App
python object_detector.py


App runs at:

👉 http://127.0.0.1:5001/

🧪 Example Output (JSON)
[
  {
    "bbox": [670, 273, 770, 365],
    "color": "#FFCC00",
    "label": "Medium Deep Caries (69%)",
    "probability": 0.69,
    "severity": "Medium"
  },
  {
    "bbox": [605, 299, 727, 417],
    "color": "#34C759",
    "label": "Low Deep Caries (42%)",
    "probability": 0.42,
    "severity": "Low"
  }
]

📜 Academic Note

This project was developed as part of CPS843 – Introduction to Computer Vision at TMU.
It demonstrates:
Image pre-processing
Bounding box visualization
AI model integration
Convolution-based sharpening
Web UI development

📚 References

This project builds upon publicly available research, datasets, and tools that contributed to the development of the cavity-detection system.

1. Dentex Dataset (Roboflow Universe)

The AI model used for detecting caries and deep caries is based on the publicly accessible Dentex dataset:
https://universe.roboflow.com/dentex/dentex-3xe7e

This dataset provides annotated dental X-ray images used for training and evaluation of object detection models on dental cavities.

2. DentalXrayAI – YOLOv8 Training Reference

The cavity detection workflow, training pipeline structure, preprocessing ideas, and model integration approaches were partially inspired by:
https://github.com/NoahOksuz/DentalXrayAI

This repository explores YOLO-based cavity detection on dental X-rays and contributed to architectural inspiration for this project.

3. Roboflow Inference API

The real-time detection in this project uses the Roboflow Hosted Inference API:
https://roboflow.com

This API provides YOLOv8 inference endpoints that deliver bounding boxes, class predictions, and confidence scores.

4. TMU – CPS843 Course Material

General computer vision concepts used here (image processing, canvas rendering, convolution sharpening) are based on the topics and principles taught in CPS843 at Toronto Metropolitan University.
