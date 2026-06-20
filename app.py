import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('House_prediction.pkl', 'rb'))

st.header('Bangalore House Prices Predictor')

data = pd.read_csv('Cleaned_data.csv')

loc = st.selectbox('Choose the location', data['location'].unique())

sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter No of Bedrooms')
bath = st.number_input('Enter No of Bathrooms')
balc = st.number_input('Enter No of Balconies')

input_df = pd.DataFrame(
    [[loc, sqft, bath, balc, beds]],
    columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms']
)

if st.button('Predict Price'):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Price: ₹ {prediction:.2f} Lakhs")