def predict_failure(wear):
    if wear > 0.8:
        return "High Risk"
    elif wear > 0.5:
        return "Medium Risk"
    return "Safe"
