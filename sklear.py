from sklearn import datasets
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# data1=datasets.fetch_20newsgroups()
# # print(data1.__len__)
# print(data1.target[:100])
##33-45 in note
X,y=make_classification(n_samples=300,flip_y=0.1,class_sep=2.5,n_classes=4,n_redundant=1,n_clusters_per_class=1,n_features=5)
print(X.all)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
plt.show()