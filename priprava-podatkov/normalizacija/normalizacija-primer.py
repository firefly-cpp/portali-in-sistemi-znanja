import numpy as np

val = np.array([3, 5, 6, 9, 10, 12, 14, 15])

min_val = np.min(val)
max_val = np.max(val)

normalized = [0.0] * len(val)
for i in range(len(val)):
    normalized[i] = np.round(((val[i] - min_val) / (max_val - min_val)), decimals=2)

print (normalized)
    
