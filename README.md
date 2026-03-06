🌲 Algerian Forest Fire Prediction – ML Web App

A production-ready Machine Learning web application that predicts the Fire Weather Index (FWI) using meteorological and fire weather index parameters from Algerian forest data.
The application is built using Flask and deployed on Render for scalable cloud-based inference.

🚀 Live Application

Live URL:
https://algerian-forest-1.onrender.com

🧠 Problem Statement

Forest fires cause severe environmental and economic damage. Early prediction of fire risk helps authorities take preventive measures and manage resources effectively.

This project predicts the Fire Weather Index (FWI) using meteorological conditions and fire weather indices from Algerian forest regions. The system allows users to input environmental parameters and instantly receive predictions through a web interface.

📊 Dataset

Dataset Name: Algerian Forest Fires Dataset

Regions Covered:
Bejaia
Sidi Bel-Abbes

The dataset contains meteorological observations and fire weather indices collected from Algerian forests.

🔢 Input Features

Temperature
Relative Humidity (RH)
Wind Speed (Ws)
Rain
FFMC (Fine Fuel Moisture Code)
DMC (Duff Moisture Code)
ISI (Initial Spread Index)
Classes (Fire / No Fire)
Region (Bejaia / Sidi Bel-Abbes)

🛠️ Tech Stack

Machine Learning

Python 3.10
NumPy
Pandas
Scikit-learn
Ridge Regression

Web Development

Flask
HTML
CSS

Deployment

Gunicorn
Render

☁️ Cloud Deployment

Application deployed on Render as a Web Service
Gunicorn used as production WSGI server
Python runtime environment used for hosting
Real-time prediction system for machine learning inference

📈 Model Details

Algorithm: Ridge Regression

Preprocessing: Standard Scaling

Python Version: 3.10

Model Persistence: Pickle (.pkl files)
✅ Key Learnings

End-to-end machine learning project workflow
Data preprocessing and feature engineering
Model training and evaluation
Model serialization using Pickle
Building a Flask web application for ML models
Deploying machine learning applications on cloud platforms
Handling real-world deployment issues

👤 Author

Somojeet Paul

Aspiring Machine Learning Engineer

GitHub:
https://github.com/Somojeet123

LinkedIn:
www.linkedin.com/in/somojeet-paul
