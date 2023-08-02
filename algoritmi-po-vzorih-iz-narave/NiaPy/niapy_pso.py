from niapy.algorithms.basic import ParticleSwarmAlgorithm
from niapy.task import Task
from niapy.problems import Sphere

algoritem = ParticleSwarmAlgorithm(
    population_size=50, min_velocity=-4.0, max_velocity=4.0
)

# izvedemo 25 zagonov algoritma PSO
for i in range(25):
    task = Task(problem=Sphere(dimension=10, lower=-
                600, upper=600), max_evals=10000)
    best = algoritem.run(task=task)
    print("%s -> %f" % (best[0], best[1]))
print(algoritem.get_parameters())
