import os
from matplotlib import pyplot as plt
from niaarm import Dataset, get_rules
from niaarm.visualize import hill_slopes

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', 'podatkovne-zbirke', 'Abalone.csv'
)
dataset = Dataset(path)
metrics = ('support', 'confidence')
rules, _ = get_rules(dataset, 'DifferentialEvolution',
                     metrics, max_evals=1000, seed=1234)
some_rule = rules[150]
hill_slopes(some_rule, dataset.transactions)
plt.show()
