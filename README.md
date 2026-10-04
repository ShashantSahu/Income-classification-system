Bilkul bhai. **Tumhare diye hue Stock ML Predictor README ke same professional style/flow mein**, but tumhare **Income Classification System** ke according final version ye raha.

**Bas `YOUR_RENDER_WEBSITE_LINK` ko apne actual Render URL se replace kar dena.** 👇

````markdown
# 📊 Income Classification System

🌐 **Live Website: https://income-classification-system.onrender.com/

An intelligent web-based machine learning application that predicts whether a person's income belongs to the `<=50K` or `>50K` income category based on demographic, educational, employment, and financial information.

The system uses **Logistic Regression** and **Decision Tree Classifier** models and provides model evaluation, prediction probability, and an interactive web interface built with Flask.

---

## 🎯 Project Objective

The objective of this project is to develop a machine learning-based **Income Classification System** that can predict a person's income category from various personal and employment-related attributes.

The system focuses on:

- Encoding categorical features such as education, occupation, work class, and marital status
- Training classification models
- Comparing model performance
- Predicting income categories
- Evaluating models using standard classification metrics
- Providing predictions through a web-based interface

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ShashantSahu/Income-classification-system.git
cd Income-classification-system
````

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the Models

```bash
python train_model.py
```

### 6. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Models

The system implements two machine learning classification algorithms:

### 1. Logistic Regression

Logistic Regression is used for binary classification to predict whether a person's income is `<=50K` or `>50K`.

### 2. Decision Tree Classifier

Decision Tree Classifier uses a tree-based decision-making approach to classify individuals into the appropriate income category.

---

## 📋 Features Used

The system uses the following input features:

* **Age**
* **Education**
* **Work Class**
* **Occupation / Job**
* **Marital Status**
* **Sex**
* **Hours per Week**
* **Capital Gain**
* **Capital Loss**

Categorical features are encoded before being provided to the machine learning models.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Categorical Feature Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Logistic Regression / Decision Tree
   ↓
Model Evaluation
   ↓
Income Prediction
```

---

## 📊 Model Evaluation

The trained models are evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**

These metrics are used to understand and compare the classification performance of the implemented models.

---

## 🌐 Web Application

The project provides an interactive Flask-based web application with the following sections:

### 🏠 Dashboard

Provides an overview of the Income Classification System along with dataset and model-related information.

### 🔮 Income Prediction

Users can enter personal, educational, employment, and financial information to predict the income category.

The prediction page provides:

* Predicted Income Category
* Selected Machine Learning Model
* Prediction Probability

### 📈 Model Performance

Displays the performance of the implemented machine learning models using evaluation metrics and confusion matrix results.

---

## 📂 Project Structure

```text
Income-classification-system/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── README.md
│
├── model/
│   ├── models.joblib
│   ├── metrics.json
│   ├── .gitignore
│   └── .gitkeep
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── index.html
│   └── performance.html
│
└── static/
    └── style.css
```

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **HTML5**
* **CSS3**

---

## 📦 Dataset

The project is based on the **UCI Adult Income Dataset**.

The dataset contains demographic, educational, employment, and financial attributes that can be used to classify individuals into different income categories.

---

## ⭐ Key Features

* Machine Learning-based Income Classification
* Logistic Regression
* Decision Tree Classifier
* Categorical Feature Encoding
* Interactive Flask Web Application
* Income Category Prediction
* Prediction Probability
* Model Performance Comparison
* Accuracy, Precision, Recall and F1-Score
* Confusion Matrix
* Responsive Web Interface
* Cloud Deployment Support

---

## ☁️ Deployment

The application is deployed using **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## 👨‍💻 Developer

**Shashant Sahu**

B.Tech Computer Science & Engineering

**Project:** Income Classification System

**Project Type:** Minor Project — Machine Learning

---

## 📌 Academic Project

This project demonstrates the complete machine learning workflow, including data preprocessing, categorical feature encoding, model training, evaluation, prediction, web application development, and deployment.

---

## 📄 License

This project is developed for academic and educational purposes.

```

**Ye wala final professional version hai** — GitHub README mein direct paste kar sakte ho. बस ऊपर `YOUR_RENDER_WEBSITE_LINK` को अपने actual Render URL से replace करना है.
```
