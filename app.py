import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Building Cooling Load Prediction",
    page_icon="🏢",
    layout="wide"
)

# -----------------------------------------------------
# Load Trained Model
# -----------------------------------------------------
model = joblib.load("decision_tree_cooling_model.pkl")

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------
st.sidebar.title("🏢 Building Cooling Load Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Dataset")
st.sidebar.write("Energy Efficiency Dataset")
st.sidebar.write("768 Samples")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 Model")
st.sidebar.write("Decision Tree Regressor")
st.sidebar.write("R² Score : 0.967")

st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 Developer")
st.sidebar.write("Mubashir Ali")
st.sidebar.write("Mechanical Engineer")
st.sidebar.write("Machine Learning Project")

# -----------------------------------------------------
# Main Title
# -----------------------------------------------------
st.title("🏢 Building Cooling Load Prediction")

st.write(
    """
Predict the cooling energy requirement of a building
using machine learning based on its structural characteristics.
"""
)

st.markdown("---")

# -----------------------------------------------------
# Input Section
# -----------------------------------------------------
st.subheader("📋 Building Parameters")

col1, col2 = st.columns(2)

with col1:
    relative_compactness = st.number_input(
        "Relative Compactness",
        min_value=0.50,
        max_value=1.00,
        value=0.82,
        step=0.01
    )

    surface_area = st.number_input(
        "Surface Area",
        value=650.0
    )

    wall_area = st.number_input(
        "Wall Area",
        value=320.0
    )

with col2:
    roof_area = st.number_input(
        "Roof Area",
        value=120.0
    )

    overall_height = st.number_input(
        "Overall Height",
        value=7.0
    )

    glazing_area = st.number_input(
        "Glazing Area",
        min_value=0.0,
        max_value=0.4,
        value=0.25,
        step=0.05
    )

st.markdown("")

# -----------------------------------------------------
# Prediction Button
# -----------------------------------------------------
if st.button("🔍 Predict Cooling Load", use_container_width=True):

    input_data = pd.DataFrame(
        [[
            relative_compactness,
            surface_area,
            wall_area,
            roof_area,
            overall_height,
            glazing_area
        ]],
        columns=[
            "Relative_Compactness",
            "Surface_Area",
            "Wall_Area",
            "Roof_Area",
            "Overall_Height",
            "Glazing_Area"
        ]
    )

    prediction = model.predict(input_data)

    st.markdown("---")

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="Predicted Cooling Load",
        value=f"{prediction[0]:.2f} kWh/m²"
    )

# -----------------------------------------------------
# About Section
# -----------------------------------------------------
st.markdown("---")

with st.expander("ℹ About This Project"):

    st.write("""
**Project Title**

Building Cooling Load Prediction Using Machine Learning

**Dataset**

UCI Energy Efficiency Dataset

**Target Variable**

Cooling Load

**Input Features**

- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Glazing Area

**Machine Learning Algorithm**

Decision Tree Regressor

**Purpose**

Predict the cooling load of a building using its
design characteristics.
""")

# -----------------------------------------------------
# Footer
# -----------------------------------------------------
st.markdown("---")

st.caption(
    "Building Cooling Load Prediction | Developed using Streamlit and Scikit-learn"
)