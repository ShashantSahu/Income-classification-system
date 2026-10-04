# Income Classification System

A Flask-based machine learning minor project that predicts whether a person's income belongs to the `<=50K` or `>50K` category using the UCI Adult dataset.

## Mandatory project requirements covered
- Encode categorical features including education, occupation/job and marital status.
- Logistic Regression model.
- Decision Tree model.
- Evaluation using Accuracy, Precision, Recall, F1-score and Confusion Matrix.
- Final output: predicted income category.

## Run in VS Code

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

Open `http://127.0.0.1:5000`.

## Pages
- `/` — Dashboard
- `/predict` — Income prediction form
- `/performance` — Model evaluation and confusion matrices

## Deployment
The project includes a `Procfile` for Gunicorn-based deployment on services that support Python web applications. Before deployment, run `python train_model.py` so `model/models.joblib` and `model/metrics.json` are generated and included in the deployment source.
