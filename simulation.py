import pandas as pd

def simulate(model, df, X, sensitive, new_value):

    sample = df.iloc[0:1].copy()
    original = sample.copy()

    sample[sensitive] = new_value

    sample_enc = pd.get_dummies(sample)
    sample_enc = sample_enc.reindex(columns=X.columns, fill_value=0)

    new_pred = model.predict(sample_enc)[0]

    original_enc = pd.get_dummies(original)
    original_enc = original_enc.reindex(columns=X.columns, fill_value=0)

    old_pred = model.predict(original_enc)[0]

    return old_pred, new_pred, sample