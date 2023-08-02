# povzeto po: https://github.com/NiaOrg/NiaPy-examples/tree/master/optimize_KNN_parameters
def get_hyperparameters(x):
    """Get hyperparameters for solution `x`."""
    algorithms = ('ball_tree', 'kd_tree', 'brute')
    n_neighbors = int(5 + x[0] * 10)
    weights = 'uniform' if x[1] < 0.5 else 'distance'
    algorithm = algorithms[int(x[2] * 2)]
    leaf_size = int(10 + x[3] * 40)

    params = {
        'n_neighbors': n_neighbors,
        'weights': weights,
        'algorithm': algorithm,
        'leaf_size': leaf_size
    }
    return params


sol = [0.4, 0.22, 0.70, 0.79]

parametri = get_hyperparameters(sol)

print(parametri)
