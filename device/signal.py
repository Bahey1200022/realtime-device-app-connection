import numpy as np
import random

def generate_ecg_signal():
    duration = random.uniform(1, 10)  # Random duration between 1 and 10 seconds
    sampling_rate = random.randint(100, 1000)  # Random sampling rate between 100 and 1000 Hz

    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    ecg_signal = np.sin(2 * np.pi * 1 * t) + np.sin(2 * np.pi * 0.5 * t) + np.sin(2 * np.pi * 2 * t)
    
    return t, ecg_signal