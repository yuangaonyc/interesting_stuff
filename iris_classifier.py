# TensorFlowLinearClassifier classification model
import tensorflow as tf
from sklearn import datasets, metrics

iris = datasets.load_iris()

classifier = tf.contrib.learn.TensorFlowLinearClassifier(n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)