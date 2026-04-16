import pandas as pd

def clean_data(df, target):
    df = df.dropna()
    df = df.apply(lambda x: x.astype(str).str.strip())

    df[target] = df[target].replace({
        "<=50K": 0, ">50K": 1,
        "<=50K.": 0, ">50K.": 1
    })

    df[target] = pd.to_numeric(df[target], errors='coerce')
    df = df.dropna()

    return df