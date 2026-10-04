📊 Income Classification System — Shashant Sahu

A complete ML-powered income classification web app built with **Flask**, **scikit-learn**, and the **UCI Adult Income Dataset**.

The system predicts whether a person's income belongs to the `<=50K` or `>50K` category using machine learning classification models.


🌐 **Live Website:** https://income-classification-system.onrender.com/

---

 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train the ML models
python train_model.py

# 3. Run the Flask app
python app.py
````

---

 📦 Project Structure

```text
Income-classification-system/
├── app.py              ← Main Flask application
├── train_model.py      ← Data preprocessing + model training
├── requirements.txt    ← Python dependencies
├── Procfile            ← Render deployment configuration
├── README.md
│
├── model/
│   ├── models.joblib   ← Trained ML models
│   ├── metrics.json    ← Model evaluation metrics
│   ├── .gitignore
│   └── .gitkeep
│
├── templates/
│   ├── base.html       ← Base layout
│   ├── dashboard.html  ← Dashboard
│   ├── index.html      ← Prediction page
│   └── performance.html← Model performance
│
└── static/
    └── style.css       ← Website styling
```

---

🤖 ML Models Available

| **Model**           | **Best For**                               |
| ------------------- | ------------------------------------------ |
| Logistic Regression | Simple, fast, interpretable classification |
| Decision Tree       | Rule-based, non-linear classification      |

---

📋 Features Used

* Age
* Education
* Work Class
* Occupation / Job
* Marital Status
* Sex
* Hours per Week
* Capital Gain
* Capital Loss

Categorical features such as **Education, Work Class, Occupation, and Marital Status** are encoded before model training and prediction.

---

 📊 Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The application also provides a **Model Performance** section for comparing the implemented classifiers.

---

🔮 Prediction

Enter the required personal and employment information and select a model to predict:

* `<=50K`
* `>50K`

The application also displays the **prediction probability** and the **model used**.

---

 🔄 ML Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Income Prediction
```

---

🛠️ Technologies Used

* **Python**
* **Flask**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **HTML5**
* **CSS3**

---

🌐 Deployment

The application is deployed using **Render**.

Build Command

```bash
pip install -r requirements.txt
```

 Start Command

```bash
gunicorn app:app
```

---

🎯 Project Objective

To develop a machine learning-based system that predicts a person's income category using demographic, educational, employment, and financial attributes.

---

👨‍💻 Developer

**Shashant Sahu**


B.Tech Computer Science & Engineering
