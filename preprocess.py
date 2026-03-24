import numpy as np

def prepare_input(data, scaler):
    data = np.array(data).reshape(1, -1)
    data_scaled = scaler.transform(data)

    # LSTM fix
    return data_scaled.reshape(1, 1, data_scaled.shape[1])
