# DeepFake Detector

A modern web application for detecting deepfakes in video files using advanced AI and deep learning.

---

## 🚀 Features

- **Upload a video** and get a deepfake probability score.
- **Visual feedback:** Deepfake frames are highlighted in the output video.
- **Modern UI:** Responsive, animated frontend with parallax effects.
- **Easy to use:** Simple web interface, no coding required.
- **Open source:** Easily extensible for research or production.

---

## 🏗️ Architecture Overview

```
User
 │
 │  (1) Uploads video via web UI
 ▼
Frontend (Flask + HTML/CSS/JS)
 │
 │  (2) Sends video to backend
 ▼
Backend (Flask, Python)
 │
 │  (3) Processes video:
 │      - Face detection (MTCNN)
 │      - Face feature extraction (InceptionResnetV1)
 │      - Frame similarity analysis
 │      - Annotates deepfake frames
 │
 │  (4) Returns results and annotated video
 ▼
User
```

- **Frontend:** Modern HTML/CSS/JS (Bootstrap, AOS, particles.js) served by Flask.
- **Backend:** Python Flask app with deep learning models for video analysis.
- **Model:** Uses `facenet_pytorch` (MTCNN for face detection, InceptionResnetV1 for feature extraction).
- **No large model files in repo:** All models are loaded via pip or downloaded at runtime.

---

## 🖥️ Local Setup

```bash
# 1. Upgrade pip and install dependencies
pip install -U pip wheel setuptools
pip install -r requirements.txt

# 2. Run the Flask app
python main.py

# 3. Open your browser at
http://127.0.0.1:5000
```

---

## ⚙️ How It Works

1. **Video Upload:** User uploads a video file via the web interface.
2. **Frame Extraction:** The backend reads the video and extracts frames.
3. **Face Detection:** Each frame is processed with MTCNN to detect faces.
4. **Feature Extraction:** Detected faces are converted to feature vectors using InceptionResnetV1.
5. **Similarity Analysis:** Consecutive frames' faces are compared for similarity.
6. **Deepfake Detection:** If similarity drops below a threshold for several frames, those frames are marked as deepfake.
7. **Result Video:** The output video is generated with red (deepfake) and green (real) boxes and labels.
8. **Results Display:** The user sees the annotated video and a deepfake probability score.

---

## 📝 Deployment Notes

- **Vercel/Serverless:** Not suitable for backend/model inference due to size limits. Use platforms like Railway, Render, AWS EC2, or Azure for backend deployment.
- **Frontend:** Can be deployed on Vercel/Netlify as a static site if backend is hosted elsewhere.
- **Large files:** Do not commit large model files to the repo. Use external storage and download at runtime if needed.

---

## 🤝 Contributing

We welcome contributions!

- **Fork** this repo and clone it.
- **Create a branch** for your feature or bugfix.
- **Commit** with clear messages.
- **Push** to your fork and **open a pull request**.

---

## 📂 Project Structure

```
deepfake-master/
│
├── main.py                # Flask app entry point
├── deepfake_detector.py   # Deepfake detection logic
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates (frontend)
├── static/                # Static assets (CSS, JS, images, videos)
│   ├── img/
│   └── videos/
└── README.md              # This file
```

---

## 📚 References

- [facenet-pytorch](https://github.com/timesler/facenet-pytorch)
- [OpenCV](https://opencv.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)

---



