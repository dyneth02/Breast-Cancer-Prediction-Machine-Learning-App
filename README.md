# Breast Cancer Diagnosis ML Web Application

## 📋 Project Overview
An end-to-end machine learning application for breast cancer diagnosis that predicts whether a breast mass is benign or malignant based on cytology lab measurements. The project includes both model training and an interactive web interface.

## 🚀 Features

### **1. Machine Learning Pipeline**
- Data preprocessing and cleaning from the Wisconsin Breast Cancer Dataset
- Feature scaling using StandardScaler
- Logistic Regression classification model
- Model evaluation with accuracy metrics and classification reports
- Serialized model and scaler for production use

### **2. Interactive Web Application (Streamlit)**
- Real-time interactive sliders for 30+ cell nuclei measurements
- Dynamic radar chart visualization comparing:
  - Mean values
  - Standard error values
  - Worst-case values
- Instant prediction results with probability scores
- Responsive two-column layout design

### **3. Key Functionalities**
- **Data Cleaning**: Automatic handling of missing values and column mapping
- **Feature Scaling**: Min-max scaling for visualization and model input
- **Model Prediction**: Real-time inference with probability outputs
- **Visual Analytics**: Plotly-based radar charts for multi-dimensional data visualization
- **User-Friendly Interface**: Intuitive sidebar controls and clear result displays

## 📁 Project Structure
├── main.py # Streamlit web application
├── model_training.py # ML model training script
├── model.pkl # Trained logistic regression model
├── scaler.pkl # Fitted StandardScaler object
├── dataset/
│ └── cdata.csv # Breast cancer dataset
├── requirements.txt # Python dependencies
└── README.md # This file
