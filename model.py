from sklearn.linear_model import LogisticRegression
import pandas as pd

def train_model(df, target, sensitive):

    safe_cols = []

    for col in df.columns:
        if col != target and col != sensitive:
            try:
                df[col] = pd.to_numeric(df[col])
                safe_cols.append(col)
            except:
                continue

    safe_cols.append(sensitive)

    X = df[safe_cols]
    y = df[target]

    X = pd.get_dummies(X, drop_first=True)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    preds = model.predict(X)

    return model, X, preds
def run_model():
    # your existing training code
    
    accuracy = 0.85   # ⚠️ replace with real accuracy
    return accuracy