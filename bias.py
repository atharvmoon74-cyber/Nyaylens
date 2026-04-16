def calculate_bias(df, sensitive):

    groups = df[sensitive].unique()

    if len(groups) < 2:
        return None, None, None

    g1 = df[df[sensitive] == groups[0]]['pred']
    g2 = df[df[sensitive] == groups[1]]['pred']

    bias = abs(g1.mean() - g2.mean())
    fairness = 1 - bias

    return bias, fairness, groups
def get_bias_score():
    # your existing code runs here
    
    fairness = 0.23   # ⚠️ replace this with your actual computed fairness
    message = "Model shows slight bias"

    return fairness, message