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
```
  ├── main.py # Streamlit web application
  ├── model_training.py # ML model training script
  ├── model.pkl # Trained logistic regression model
  ├── scaler.pkl # Fitted StandardScaler object
  ├── dataset/
  │ └── cdata.csv # Breast cancer dataset
  ├── requirements.txt # Python dependencies
  └── README.md # This file
```


## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/breast-cancer-prediction.git
   cd breast-cancer-prediction
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the web application:
   ```bash
   streamlit run main.py

## Dependencies (requirements.txt)
   ```bash
   streamlit==1.28.0
   pandas==2.0.3
   numpy==1.24.3
   scikit-learn==1.3.0
   plotly==5.17.0 
   ```

## 🧪 Model Training
  To retrain the model:
  ```bash
   python model_training.py
  ```

This will:
  1. Load and clean the dataset
  2. Split data into training and testing sets
  3. Train a logistic regression model
  4. Evaluate model performance
  5. Save the model and scaler as .pkl files

## 🎮 Using the Application

  1. Adjust Measurements: Use the sidebar sliders to input cell nuclei measurements
  2. View Visualization: Observe the radar chart showing three measurement categories
  3. Get Predictions: See the prediction (Benign/Malignant) with probability scores
  4. Medical Disclaimer: Always consult healthcare professionals for actual diagnoses

## 📊 Dataset Information

  1. The application uses the Wisconsin Breast Cancer Dataset containing:
  2. 569 instances with 30 features each
  3. Features include mean, standard error, and worst values of:
  4. Radius, Texture, Perimeter, Area
  5. Smoothness, Compactness, Concavity
  6. Concave Points, Symmetry, Fractal Dimension
  7. Binary target variable: Malignant (M) or Benign (B)

## 🔍 Model Performance

  1. The logistic regression model achieves:
  2. High accuracy on test data
  3. Detailed classification metrics
  4. Probability outputs for confident decision-making
