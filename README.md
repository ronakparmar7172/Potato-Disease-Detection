# Potato-Disease-Detection


An AI-powered web application that detects **potato leaf diseases** from images using a deep learning model.  
The system allows users to upload a potato leaf image and receive the predicted disease along with confidence.

---

## 📌 Project Overview

Potato diseases like **Early Blight** and **Late Blight** can significantly reduce crop yield.  
This project uses a **Convolutional Neural Network (CNN)** to classify potato leaf images and provides predictions through a **FastAPI backend** and a **React frontend**.

---

## 🚀 Features

- Upload potato leaf images
- AI-based disease prediction
- Confidence score for predictions
- Clean & user-friendly UI
- FastAPI backend for ML inference
- React frontend for interaction

---

## 🧠 Diseases Detected

- Early Blight
- Late Blight
- Healthy Leaf

---

## 🛠️ Tech Stack

### Backend
- Python
- TensorFlow / Keras
- FastAPI
- Uvicorn
- NumPy
- Pillow

### Frontend
- React.js
- JavaScript
- CSS
- Axios

---

## 📁 Project Structure
Potato_Disease/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── potato_disease_model.keras
│
├── frontend/
│ ├── src/
│ ├── package.json
│
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ronakparmar7172/Potato-Disease-Detection.git
cd Potato-Disease-Detection

2️⃣ Backend Setup

Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate   # Windows


Install dependencies:
pip install -r backend/requirements.txt


Run FastAPI server:
cd backend
uvicorn app:app --reload


Backend will run at:
http://127.0.0.1:8000
API Docs:
http://127.0.0.1:8000/docs

3️⃣ Frontend Setup
cd frontend
npm install
npm start

Frontend will run at:
http://localhost:3000


📊 How It Works

User uploads a potato leaf image
Image is sent to FastAPI backend
Image is preprocessed and passed to CNN model
Model predicts disease class
Result is returned to frontend and displayed

🧪 Model Information

Model Type: CNN
Framework: TensorFlow / Keras
Input Size: 224 × 224 RGB image
Output: Disease class + confidence score

📌 Future Improvements
Disease treatment recommendations
Prediction history
User authentication
Cloud deployment
Mobile app version

👨‍💻 Author
Ronak Parmar
AI / ML Enthusiast | IT Student

⭐ Acknowledgements
Plant disease dataset
TensorFlow & FastAPI documentation
