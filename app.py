"""Flask web application for the Income Classification System."""
import json
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

app = Flask(__name__)


def load_artifacts():
    """Load trained models and evaluation metadata if available."""
    models_path = MODEL_DIR / "models.joblib"
    metrics_path = MODEL_DIR / "metrics.json"
    if not models_path.exists() or not metrics_path.exists():
        return {}, {}
    return joblib.load(models_path), json.loads(metrics_path.read_text(encoding="utf-8"))


models, meta = load_artifacts()


def refresh_artifacts():
    global models, meta
    models, meta = load_artifacts()


@app.route("/")
def dashboard():
    results = meta.get("results", [])
    best_accuracy = max((r["accuracy"] for r in results), default=0)
    best_model = max(results, key=lambda r: r["accuracy"])["name"] if results else "—"
    return render_template(
        "dashboard.html",
        meta=meta,
        results=results,
        best_accuracy=best_accuracy,
        best_model=best_model,
    )


@app.route("/predict", methods=["GET", "POST"])
def predict():
    # Refresh so the app works immediately after train_model.py is run.
    refresh_artifacts()
    result, form = None, {}
    if request.method == "POST" and models:
        form = request.form.to_dict()
        row = pd.DataFrame([{
            "workclass": form["workclass"],
            "marital-status": form["marital-status"],
            "education": form["education"],
            "occupation": form["occupation"],
            "sex": form["sex"],
            "age": int(form["age"]),
            "capital-gain": int(form["capital-gain"] or 0),
            "capital-loss": int(form["capital-loss"] or 0),
            "hours-per-week": int(form["hours"]),
        }])
        pipe = models[form["model"]]
        high = int(pipe.predict(row)[0]) == 1
        prob = float(pipe.predict_proba(row)[0][1]) * 100
        result = {
            "label": ">50K" if high else "<=50K",
            "high": high,
            "prob": round(prob, 1),
            "model": form["model"],
        }

    return render_template(
        "index.html",
        opts=meta.get("options", {}),
        result=result,
        form=form,
        model_names=list(models),
        setup_needed=not models,
    )


@app.route("/performance")
def performance():
    refresh_artifacts()
    return render_template("performance.html", meta=meta)


if __name__ == "__main__":
    app.run(debug=True)
