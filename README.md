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

This project uses public sources that shaped the model flow, the image work, and the viewer. The list below shows the main items that helped guide the work.

1. Dentex Dataset (Roboflow Universe)
The model in this project uses the Dentex dataset for caries and deep caries. The dataset provides labelled dental X-rays with two classes. These samples helped us see how decay appears in real cases.
https://universe.roboflow.com/dentex/dentex-3xe7e

2. DentalXrayAI (GitHub)
This open-source project showed how dental X-rays can pass through a YOLO model. We used this as a guide when planning the folder layout and the flow from upload to detection.
https://github.com/NoahOksuz/DentalXrayAI

3. Roboflow Hosted Inference API
The tool sends each uploaded X-ray to the Roboflow API. The API returns boxes, class names, and confidence values. This keeps the model work simple and steady on a local setup.
https://roboflow.com

4. YOLOv8 (Ultralytics)
YOLOv8 is the base model used by the API. It supports fast inference and clean output. We reviewed the public notes on the model to understand how the boxes and scores are produced.
https://github.com/ultralytics/ultralytics

5. YOLO: You Only Look Once (Redmon et al.)
This paper introduced the first YOLO model. It explains how one network can predict boxes and class names at the same time. We used this to understand the idea behind our own detection step.
https://arxiv.org/abs/1506.02640

6. YOLOv4 (Bochkovskiy et al.)
This version of YOLO shows ways to improve speed and accuracy. It helped us understand why modern models like YOLOv8 work well on clean datasets such as Dentex.
https://arxiv.org/abs/2004.10934

7. CVPR Open Access (CVF)
We reviewed open-access pages from CVPR to see how object detection is tested across other tasks. This helped us place our own detection work in a simple context.
http://openaccess.thecvf.com

8. arXiv Computer Vision Section
We checked the Computer Vision section on arXiv to review papers related to object detection and image tasks. This step helped us see how bounding boxes and filters are used in other projects.
https://arxiv.org/list/cs.CV/recent

9. CPS843 Course Material (TMU)
The viewer uses ideas from CPS843 such as spatial filters, cropping, and sharpening. These concepts shaped the steps used to build the cavity viewer.

10. Project Repository
The full source code for this tool is available here:
https://github.com/singlasatwik16-collab/Cavity_Detection_Xray_CPS843
