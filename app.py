import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load("house_price_model.pkl")
except:
    model = joblib.load("house_price_model_pkl")

st.title("🏠 House Price Prediction")
st.write("Enter house details to predict sale price")

feature_names = model.feature_names_in_

input_data = pd.DataFrame(0, index=[0], columns=feature_names)

def set_value(col, value):
    if col in input_data.columns:
        input_data[col] = value

OverallQual = st.slider("Overall Quality", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area", value=1500)
GarageCars = st.number_input("Garage Cars", value=2)
GarageArea = st.number_input("Garage Area", value=500)
TotalBsmtSF = st.number_input("Total Basement Area", value=800)
FirstFlrSF = st.number_input("First Floor Area", value=1000)
FullBath = st.number_input("Full Bathrooms", value=2)
YearBuilt = st.number_input("Year Built", value=2000)
YearRemodAdd = st.number_input("Year Remodelled", value=2005)
TotRmsAbvGrd = st.number_input("Total Rooms Above Ground", value=6)
Fireplaces = st.number_input("Fireplaces", value=1)
LotArea = st.number_input("Lot Area", value=8000)

Neighborhood = st.selectbox("Neighborhood", ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst"])
HouseStyle = st.selectbox("House Style", ["1Story", "2Story", "1.5Fin"])
ExterQual = st.selectbox("Exterior Quality", ["TA", "Gd", "Ex", "Fa"])
KitchenQual = st.selectbox("Kitchen Quality", ["TA", "Gd", "Ex", "Fa"])
CentralAir = st.selectbox("Central Air", ["Y", "N"])

set_value("OverallQual", OverallQual)
set_value("GrLivArea", GrLivArea)
set_value("GarageCars", GarageCars)
set_value("GarageArea", GarageArea)
set_value("TotalBsmtSF", TotalBsmtSF)
set_value("1stFlrSF", FirstFlrSF)
set_value("FullBath", FullBath)
set_value("YearBuilt", YearBuilt)
set_value("YearRemodAdd", YearRemodAdd)
set_value("TotRmsAbvGrd", TotRmsAbvGrd)
set_value("Fireplaces", Fireplaces)
set_value("LotArea", LotArea)

for col in [
    f"Neighborhood_{Neighborhood}",
    f"HouseStyle_{HouseStyle}",
    f"ExterQual_{ExterQual}",
    f"KitchenQual_{KitchenQual}",
    f"CentralAir_{CentralAir}"
]:
    if col in input_data.columns:
        input_data[col] = 1

if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏠 Predicted House Price: ${prediction:,.2f}")