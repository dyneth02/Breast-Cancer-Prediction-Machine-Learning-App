import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import plotly.graph_objects as go

def get_cleaned_data():
    uncleaned_data = pd.read_csv("../dataset/cdata.csv")
    uncleaned_data = uncleaned_data.drop(["Unnamed: 32", "id"], axis=1)
    uncleaned_data["diagnosis"] = uncleaned_data["diagnosis"].map(
        { "M" : 1,
          "B" : 0
        }
    )
    cleaned_data = uncleaned_data
    return cleaned_data

def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")
    data = get_cleaned_data()
    slider_labels = {
        "Radius (mean)": "radius_mean",
        "Texture (mean)": "texture_mean",
        "Perimeter (mean)": "perimeter_mean",
        "Area (mean)": "area_mean",
        "Smoothness (mean)": "smoothness_mean",
        "Compactness (mean)": "compactness_mean",
        "Concavity (mean)": "concavity_mean",
        "Concave points (mean)": "concave points_mean",
        "Symmetry (mean)": "symmetry_mean",
        "Fractal dimension (mean)": "fractal_dimension_mean",

        "Radius (se)": "radius_se",
        "Texture (se)": "texture_se",
        "Perimeter (se)": "perimeter_se",
        "Area (se)": "area_se",
        "Smoothness (se)": "smoothness_se",
        "Compactness (se)": "compactness_se",
        "Concavity (se)": "concavity_se",
        "Concave points (se)": "concave points_se",
        "Symmetry (se)": "symmetry_se",
        "Fractal dimension (se)": "fractal_dimension_se",

        "Radius (worst)": "radius_worst",
        "Texture (worst)": "texture_worst",
        "Perimeter (worst)": "perimeter_worst",
        "Area (worst)": "area_worst",
        "Smoothness (worst)": "smoothness_worst",
        "Compactness (worst)": "compactness_worst",
        "Concavity (worst)": "concavity_worst",
        "Concave points (worst)": "concave points_worst",
        "Symmetry (worst)": "symmetry_worst",
        "Fractal dimension (worst)": "fractal_dimension_worst",
    }
    inputs = {}
    for label, data_col in slider_labels.items():
        col_min = float(data[data_col].min())
        col_max = float(data[data_col].max())
        default = float(data[data_col].mean())

        inputs[data_col] = st.sidebar.slider(
            label=label,
            min_value=col_min,
            max_value=col_max,
            value=default,
            step=(col_max - col_min) / 100 if (col_max - col_min) > 0 else 0.01,
            key=f"slider_{data_col}",
        )
    return inputs

def get_scaled_values(input_data):
    data = get_cleaned_data()

    X = data.iloc[:,1:]
    y = data.iloc[:,0]

    scaled_dict = {}

    for key,value in input_data.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_val = ((value - min_val) / (max_val - min_val)) * 10
        scaled_dict[key] = scaled_val

    return scaled_dict

def get_radar_chart(input_data):
    input_data = get_scaled_values(input_data)
    categories = [
        "Radius",
        "Texture",
        "Perimeter",
        "Area",
        "Smoothness",
        "Compactness",
        "Concavity",
        "Concave points",
        "Symmetry",
        "Fractal dimension"
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_mean'],
            input_data['texture_mean'],
            input_data['perimeter_mean'],
            input_data['area_mean'],
            input_data['smoothness_mean'],
            input_data['compactness_mean'],
            input_data['concavity_mean'],
            input_data['concave points_mean'],
            input_data['symmetry_mean'],
            input_data['fractal_dimension_mean']
        ],
        theta=categories,
        fill='toself',
        name='Mean'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_se'],
            input_data['texture_se'],
            input_data['perimeter_se'],
            input_data['area_se'],
            input_data['smoothness_se'],
            input_data['compactness_se'],
            input_data['concavity_se'],
            input_data['concave points_se'],
            input_data['symmetry_se'],
            input_data['fractal_dimension_se']
        ],
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_worst'],
            input_data['texture_worst'],
            input_data['perimeter_worst'],
            input_data['area_worst'],
            input_data['smoothness_worst'],
            input_data['compactness_worst'],
            input_data['concavity_worst'],
            input_data['concave points_worst'],
            input_data['symmetry_worst'],
            input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill='toself',
        name='Worst Value'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False
    )
    return fig

def add_predictions(input_data):
    model = pkl.load(open("../model.pkl", "rb"))
    scaler = pkl.load(open("../scaler.pkl", "rb"))
    input_array = np.array(list(input_data.values())).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)
    predictions = model.predict(input_array_scaled)

    st.subheader("Cell Cluster Prediction")
    st.write("The Cell Cluster prediction is")

    if predictions[0] == 0:
        st.write("Benign")
    else:
        st.write("Malignant")

    st.write("Probability of being Benign: ", model.predict_proba(input_array_scaled)[0][0])
    st.write("Probability of being Malignant: ", model.predict_proba(input_array_scaled)[0][1])
    st.write("This app can assist medical professionals in making a diagnosis, but should not be used in as substitute for a professional diagnosis.")

def main():
    st.set_page_config(
        page_title="Breast Cancer Prediction Model",
        page_icon=":femail-doctor:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    input_data = add_sidebar()
    
    with st.container():
        st.title("Test the Breast - Breast Cancer Diagnosis")
        st.write("Please connect with this app to your cytology lab to help diagnose breast cancer tissue sample. This app predicts using a machine learning model whether a breast mass us benign or malignant based on the measurements it receives from your cytology lab. You can also update the measurements by hand using the sliders given in the sidebar.")

    col1, col2 = st.columns([4,1]) # 2 args = 2 columns. The ratio is 4/5 & 1/5.

    with col1:
        radar = get_radar_chart(input_data)
        st.plotly_chart(radar)
    with col2: 
        add_predictions(input_data)

if __name__ == "__main__":
    main()