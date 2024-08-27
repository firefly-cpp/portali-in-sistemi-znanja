import os
from niaarm.dataset import Dataset

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', 'podatkovne-zbirke', 'Abalone.csv'
)
data = Dataset(path)

print(data)
