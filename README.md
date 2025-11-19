# project-2
📘 Project Title: Area-Based House Price Prediction Web App
📝 Project Overview

This project is a machine learning-based web application that predicts the price of a property based on its area in square feet. The system uses a pre-trained model (areaprice.pkl) to estimate property prices. The user interacts with a simple and intuitive interface built using Streamlit, a Python framework for creating data-driven web applications.

🎯 Project Objective

The main goal of this project is to provide users with an instant property price estimate by entering the area of the house. It helps real estate agents, buyers, sellers, or investors get quick insights into pricing based on area.

🔧 Technologies Used
Component	Purpose
Python	Programming language
Streamlit	Frontend and UI framework
Pickle	To load trained ML model
Scikit-learn (likely used before saving model)	To create and train ML model
Machine Learning	To predict property prices
📂 How the Application Works

Load the Machine Learning Model

The app loads a trained model file named areaprice.pkl using Pickle.

This model was likely trained on historical area-price data.

Streamlit Web Interface

The app displays a title: Area Price Prediction.

It provides an input box where the user enters the area (in square feet).

A Predict Price button triggers the prediction.

Prediction Logic

When the button is clicked, the app sends the entered area as input to the machine learning model.

The model returns the predicted price.

The result is displayed on the screen.
