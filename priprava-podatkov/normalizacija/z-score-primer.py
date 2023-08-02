import numpy as np

val = np.array([3, 5, 6, 8, 10, 12, 14, 15])

std = np.round(np.std(val), decimals=1)

mean = np.round(np.mean(val), decimals=1)

print("Standardni odklon: ", std)
print("Povprečje:  ", mean)

new_val = [0.0] * len(val)
for i in range(len(val)):
    new_val[i] = np.round(((val[i] - mean) / std), decimals=2)

print(new_val)
