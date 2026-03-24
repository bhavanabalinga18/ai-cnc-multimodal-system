import numpy as np

def get_sensor_data():
    return [
        np.random.uniform(100,150),
        np.random.uniform(0.1,0.3),
        np.random.uniform(0.8,1.5),
        np.random.uniform(25,50),
        np.random.uniform(0.01,0.05)
    ]
