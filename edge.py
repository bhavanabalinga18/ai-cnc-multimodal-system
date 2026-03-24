def lightweight_predict(data):
    speed, feed, depth, temp, vib = data
    return speed*0.001 + feed + depth + temp*0.01 + vib*3
