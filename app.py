import streamlit as st
import pickle
import pandas as pd
import json

# --- 1. ASSET LOADING ---
@st.cache_resource
def load_assets():
    # Load the Ridge model confirmed in your notebook
    with open('RidgeModel.pkl', 'rb') as f:
        model = pickle.load(f)
    # Load the Bengaluru location list from JSON
    with open('locations.json', 'r') as f:
        locations = json.load(f)['data_columns']
    return model, locations

model, locations = load_assets()

# --- 2. HEADER SECTION ---
st.title("Bengaluru House Price Predictor")

# Updated: Removed 'home' from the project overview
st.info("**Project Overview:** Estimating Bengaluru property prices using a Ridge Regression model.")

st.write("### Enter House Details")

# --- 3. INPUT AREA ---
# Location selection with a placeholder to encourage selection
selected_location = st.selectbox("Select Location", options=[""] + locations, index=0)

col1, col2, col3 = st.columns(3)

with col1:
    # Updated: Reduced Sqft options with common Bengaluru ranges
    sqft_options = [""] + [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    total_sqft = st.selectbox("Total Sqft", options=sqft_options, index=0)

with col2:
    bath = st.selectbox("Bathrooms", options=[""] + [1, 2, 3, 4, 5], index=0)

with col3:
    bhk = st.selectbox("BHK", options=[""] + [1, 2, 3, 4, 5], index=0)

st.divider()

# --- 4. PREDICTION LOGIC & VALIDATION ---
if st.button("Calculate Predicted Price", type="primary", use_container_width=True):
    # Validation: Check if any value is still the empty placeholder
    if selected_location == "" or total_sqft == "" or bath == "" or bhk == "":
        st.warning("⚠️ Please fill in all the details before predicting the price.")
    else:
        # Prepare the input for the model
        input_df = pd.DataFrame([[selected_location, total_sqft, bath, bhk]], 
                                 columns=['location', 'total_sqft', 'bath', 'bhk'])
        
        prediction = model.predict(input_df)[0]
        
        # Display the result in a clean success box
        st.success(f"### Estimated Market Value: ₹ {prediction:.2f} Lakhs")