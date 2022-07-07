from matplotlib import pyplot as plt
from niaarm import Dataset, RuleList, get_rules
from niaarm.visualize import hill_slopes

dataset = Dataset('../podatkovne-zbirke/Abalone.csv')
metrics = ('support', 'confidence')
rules, _ = get_rules(dataset, 'DifferentialEvolution', metrics, max_evals=1000, seed=1234)
some_rule = rules[150]
hill_slopes(some_rule, dataset.transactions)
plt.show()
