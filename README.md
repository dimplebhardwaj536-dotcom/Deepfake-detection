
#  Deepfake Detection using ResNet-18

##  Overview
This project is an **ongoing** deepfake detection system built using a fine-tuned **ResNet-18** architecture. The goal is to classify facial images as **Real** or **Fake**, helping combat misinformation with deep learning.

##  Problem Statement
With the rapid rise of AI-generated deepfake images, automated tools are required to detect manipulated faces.  
This project provides a **robust and scalable** solution utilizing **ResNet-18** for image classification.

##  Key Details
- **Dataset**: 10,000 real vs. fake facial images
- **Current Status**: Ready for Deployment
- **Model**: ResNet-18 architecture
- **Training**: Applied data augmentation and fine-tuning techniques
- **Deployment**: Streamlit web app for real-time image classification

##  Features
- Automatic train/val/test split
- Extensive data augmentation for better model generalization
- Deep residual learning (ResNet-18) to avoid vanishing gradients
- Training & validation accuracy/metrics visualization
- Real-time detection interface via Streamlit
- Dropout and BatchNorm for regularization and stable training

##  Tech Stack
- **Python 3.x**
- **TensorFlow/Keras** for model training
- **NumPy, OpenCV, PIL** for image preprocessing
- **Streamlit** for web interface
- **Jupyter Notebook** for data exploration and training

## Workflow
1.  **Data Preparation**:
   - Split the raw data into train, validation, and test sets
   - Preprocessed and normalized all images
   - Applied data augmentation to increase diversity

2.  **Training**:
   - Implemented ResNet-18 with skip connections
   - Tuned hyperparameters to improve accuracy
   - Monitored training and validation metrics

3.  **Evaluation**:
   - Evaluated the model on the test set
   - Achieved a strong balance between precision and recall

4.  **Deployment**:
   - Saved the best performing model (`best_model.h5`)
   - Developed a Streamlit app for image upload and real-time predictions

##  Getting Started
###  Prerequisites
- Python 3.8+ (recommended)
- GPU (optional but recommended for training)

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd Deepfake-Detection-ResNet18-main
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the trained model file `best_model.h5` in the root directory (alongside `app.py`).

### Running the App
Start the Streamlit development server:
```bash
streamlit run app.py
```
The app will be accessible in your browser at `http://localhost:8501`.

## Deployment
This project is ready to be deployed on platforms like **Streamlit Community Cloud**, **Render**, or **Heroku**.
1. Push your code to GitHub.
2. Link your GitHub repository to your chosen deployment platform.
3. Ensure the platform installs dependencies from `requirements.txt`.
4. (Optional) If your model file `best_model.h5` is larger than 100MB, consider using Git LFS or downloading it dynamically during app startup if deploying to cloud platforms with file size limits.
