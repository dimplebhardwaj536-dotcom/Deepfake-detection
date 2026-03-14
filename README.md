<div align="center">

# 🕵️‍♂️ Deepfake Detection System
**Powered by ResNet-18 & Deep Learning**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

*An intelligent, scalable solution to combat misinformation by detecting AI-generated manipulated faces in real-time.*

</div>

---

## 🌟 Overview
With the rapid rise of AI-generated, hyper-realistic deepfake images, the need for robust automated detection tools has never been greater. 

This project provides a **state-of-the-art Deepfake Image Classifier**, built upon a fine-tuned **ResNet-18** architecture. It classifies facial images as either **Real** or **Fake** with high precision, offering a user-friendly Streamlit interface for seamless interaction.

## ✨ Key Features
- 🧠 **Deep Residual Learning:** Utilizes ResNet-18 to overcome vanishing gradients and achieve deeper network understanding.
- ⚡ **Real-Time Detection:** Instantly analyze and classify uploaded images via a sleek web interface.
- 🛡️ **Robust Generalization:** Trained on a diverse dataset of over 10,000 real vs. fake images with extensive data augmentation.
- 📊 **Confidence Metrics:** Provides a percentage confidence score alongside every prediction.

## 🛠️ Technology Stack
- **Deep Learning / Core ML:** TensorFlow 2.x, Keras
- **Computer Vision:** OpenCV, PIL (Pillow)
- **Data Processing:** NumPy
- **Frontend & Deployment:** Streamlit

## 🚀 Getting Started

Follow these clean steps to set up and run the detection system locally on your machine.

### Prerequisites
- Python 3.8 or higher installed on your system.
- (Optional but recommended) NVIDIA GPU with CUDA setup for faster inference.

### 1. Clone the Repository
```bash
git clone https://github.com/dimplebhardwaj536-dotcom/Deepfake-detection.git
cd Deepfake-detection
```

### 2. Install Dependencies
Install all required libraries securely using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Setup the Model
Ensure that your trained weights file (`best_model.h5`) is placed directly in the project's root directory (alongside `app.py`).

### 4. Launch the Application
Fire up the Streamlit server:
```bash
streamlit run app.py
```
*The application will automatically launch in your default web browser at `http://localhost:8501`.*

---

## 📈 Model Architecture & Workflow

1. **Data Pipeline:** 
   - Pre-processed and normalized face crops.
   - Robust data augmentation strategies (rotations, flips, zooming, color jitter) applied to enhance model resistance against unseen manipulations.
2. **Architecture:** 
   - Base ResNet-18 with residual skip connections.
   - Added Batch Normalization and Dropout layers at the network head to prevent overfitting and ensure stable training.
3. **Evaluation Strategy:** 
   - Optimized for a strong balance between Precision and Recall to aggressively minimize false negatives (undetected deepfakes).

## 🌐 Deployment Ready
This repository is fully modularized and ready out-of-the-box for deployment on cloud platforms such as:
- **Streamlit Community Cloud** (Recommended)
- **Render** / **Heroku**
- **AWS EC2 / Google Cloud**

*Pro-tip: If your `best_model.h5` exceeds Github's strict 100MB file limit, ensure you are utilizing Git LFS (Large File Storage) or securely downloading the weights dynamically at app runtime.*

---
<div align="center">
  <b>Built to combat digital manipulation, one pixel at a time.</b>
</div>
