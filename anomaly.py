import numpy as np

def detect_anomaly(data):
    threshold = np.mean(data) + 2*np.std(data)
    return max(data) > threshold, threshold
