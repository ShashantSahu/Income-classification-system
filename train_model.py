"""Step 1: python train_model.py  -> trains models and saves them in /model"""
import json, joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
COLS = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "income"]

# Internet na ho to Kaggle ka adult.csv "data/adult.csv" me rakh ke yahan path de do
df = pd.read_csv(URL, names=COLS, na_values="?", skipinitialspace=True)
df = df.dropna().drop_duplicates()
df["income"] = df["income"].str.contains(">50K").astype(int)   # 1 = >50K, 0 = <=50K

CAT = ["education", "workclass", "marital-status", "occupation", "sex"]
NUM = ["age", "capital-gain", "capital-loss", "hours-per-week"]
X, y = df[CAT + NUM], df["income"]

prep = ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), CAT),
                          ("num", StandardScaler(), NUM)])
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

models = {"Logistic Regression": LogisticRegression(max_iter=1000),
          "Decision Tree": DecisionTreeClassifier(max_depth=8, random_state=42)}

fitted, results = {}, []
for name, clf in models.items():
    pipe = Pipeline([("prep", prep), ("model", clf)]).fit(X_tr, y_tr)
    p = pipe.predict(X_te)
    fitted[name] = pipe
    results.append({"name": name,
                    "accuracy": round(accuracy_score(y_te, p), 4),
                    "precision": round(precision_score(y_te, p), 4),
                    "recall": round(recall_score(y_te, p), 4),
                    "f1": round(f1_score(y_te, p), 4),
                    "cm": confusion_matrix(y_te, p).tolist()})
    print(name, results[-1])

options = {c: sorted(df[c].unique().tolist()) for c in ["education", "workclass", "marital-status", "occupation", "sex"]}

joblib.dump(fitted, "model/models.joblib")
json.dump({"results": results, "options": options,
           "total_rows": len(df), "high_income_pct": round(y.mean() * 100, 1)},
          open("model/metrics.json", "w"), indent=2)
print("Saved model/models.joblib and model/metrics.json")
