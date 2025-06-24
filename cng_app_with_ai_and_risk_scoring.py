
import streamlit as st
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🚗 AI-Powered CNG Maintenance & Safety Reminder")

# --- Maintenance Section ---
st.header("🔧 Maintenance Reminder")

vehicle_name = st.text_input("Vehicle Name or Plate Number")
last_service_km = st.number_input("Last Service Odometer Reading (in KM)", min_value=0)
current_km = st.number_input("Current Odometer Reading (in KM)", min_value=0)
service_interval = st.number_input("Service Interval (in KM)", min_value=1000, value=5000)
last_service_date = st.date_input("Last Service Date")
today = datetime.today().date()
days_since_service = (today - last_service_date).days

if st.button("Check Maintenance Status"):
    km_due = current_km - last_service_km
    km_left = service_interval - km_due

    if km_due >= service_interval:
        st.warning("🔧 Service is DUE! Please service your CNG kit.")
    else:
        st.success(f"✅ Not yet due. You have {km_left} km remaining.")

    st.info(f"Days since last service: {days_since_service} days")

    # --- AI Prediction ---
    st.subheader("🧠 AI Prediction: Next Service Mileage")

    # Simulated data for demonstration
    past_km_inputs = np.array([[0], [5000], [10000], [15000]])
    expected_next_km = np.array([5000, 10000, 15000, 20000])

    model = LinearRegression()
    model.fit(past_km_inputs, expected_next_km)

    predicted_next_km = model.predict([[current_km]])[0]
    st.info(f"🔮 Predicted next service: {int(predicted_next_km)} KM")

# --- Safety Risk Assessment Section ---
st.header("🚨 CNG Leak / Safety Risk Assessment")

hissing = st.radio("Do you hear a hissing sound near or around the CNG system?", ["No", "Yes"])
smell_rating = st.slider("Rate the smell of gas inside the cabin (0 = None, 5 = Strong)", 0, 5)
check_engine = st.radio("Is the Check Engine Light ON?", ["No", "Yes"])
mileage_drop = st.radio("Has your gas mileage dropped recently?", ["No", "Yes"])
backfiring = st.radio("Has the vehicle backfired recently?", ["No", "Yes"])

if st.button("Assess Safety Risk"):
    risk_score = 0
    if hissing == "Yes": risk_score += 2
    if smell_rating >= 3: risk_score += 2
    if check_engine == "Yes": risk_score += 1
    if mileage_drop == "Yes": risk_score += 1
    if backfiring == "Yes": risk_score += 1

    if risk_score >= 5:
        st.error("🔴 High Risk – Inspect your CNG system immediately!")
    elif risk_score >= 3:
        st.warning("🟡 Moderate Risk – Monitor and consider inspection.")
    else:
        st.success("🟢 Low Risk – No immediate issue detected.")
