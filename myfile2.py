import pickle
import streamlit as st
model2 = pickle.load(open("areaprice.pkl", "rb")) 
def mydeploy():
    st.title("Area Price Prediction")
    area=st.number_input("Enter Area in square feet:")
    pred=st.button("Predict Price")

    if pred:
        X=model2.predict([[area]])
        st.write("price of given area is:", X[0])
mydeploy()
