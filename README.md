# 🌸 Cloud-Based Machine Learning Model Deployment

## Live Demo

https://cloud-ml-deployment.onrender.com

---

## Project Overview

This project is a Cloud-Based Machine Learning Model Deployment system developed using Python, Flask, and Scikit-Learn.

The application predicts the species of an Iris flower based on four input features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The trained machine learning model is deployed on the cloud and can be accessed through a web interface as well as a REST API.

---

## Features

✅ Machine Learning Model Training

✅ Random Forest Classification

✅ REST API for Predictions

✅ Cloud Deployment using Render

✅ Interactive Web Interface

✅ Prediction Logging and Monitoring

✅ GitHub Version Control

✅ Dynamic Flower Image Display

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Responsive UI Design

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Deployment

* Render Cloud Platform

### Version Control

* GitHub

### Monitoring

* Python Logging Module

---

## Dataset

The project uses the Iris Dataset provided by Scikit-Learn.

### Features Used

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## Project Architecture

User

↓

Web Interface / REST API

↓

Flask Application

↓

Random Forest Model

↓

Prediction Result

↓

Logging System

---

## REST API Endpoint

### POST Request

/api/predict

### Sample Request

```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

### Sample Response

```json
{
    "prediction": "Setosa"
}
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/DEMIGODXV5/cloud-ml-deployment.git
```

### Move into Project

```bash
cd cloud-ml-deployment
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train.py
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Monitoring

The application uses Python Logging for monitoring prediction activity.

Prediction logs are stored in:

```text
app.log
```

This helps track application usage and prediction requests.

---

## Future Enhancements

* User Authentication
* Database Integration
* Advanced Monitoring Dashboard
* Model Retraining Pipeline
* Multiple ML Algorithms
* Docker Containerization
* AWS SageMaker Deployment

---

## Learning Outcomes

* Machine Learning Model Development
* Model Serialization using Joblib
* REST API Development with Flask
* Cloud Deployment Practices
* Git and GitHub Workflow
* Logging and Monitoring
* Full Project Lifecycle Management

---

## Author

Developed by: DEMIGODXV5

Cloud-Based Machine Learning Deployment Project
