from sklearn.feature_selection import VarianceThreshold

X = [ [10, 20], [30, 40], [150, 500], [350, 10], [800, 950] ]

izbira = VarianceThreshold(threshold=0.003)

izbira.fit_transform(X)
