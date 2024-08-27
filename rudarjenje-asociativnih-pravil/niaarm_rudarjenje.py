import os
import pandas as pd
from niaarm import Dataset
from niaarm import get_rules
from niapy.algorithms.basic import DifferentialEvolution

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', 'podatkovne-zbirke', 'Abalone.csv'
)
df = pd.read_csv(path)
data = Dataset(df)

algo = DifferentialEvolution(
    population_size=50, differential_weight=0.5, crossover_probability=0.9)
metrics = ('support', 'confidence')

rules, run_time = get_rules(data, algo, metrics, max_iters=100, logging=True)

print(rules)
print(f'Run Time: {run_time}')
rules.to_csv('output.csv')
