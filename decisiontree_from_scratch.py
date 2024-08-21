import numpy as np


class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        return np.array([self._predict(inputs) for inputs in X])

    def _gini(self, y):
        m = len(y)
        return 1.0 - sum((np.sum(y == c) / m) ** 2 for c in np.unique(y))

    def _split(self, X, y, index, value):
        left_mask = X[:, index] < value
        right_mask = X[:, index] >= value
        return X[left_mask], X[right_mask], y[left_mask], y[right_mask]

    def _information_gain(self, y, y_left, y_right):
        p = float(len(y_left)) / len(y)
        return self._gini(y) - p * self._gini(y_left) - (1 - p) * self._gini(y_right)

    def _best_split(self, X, y):
        best_index, best_value, best_gain = None, None, -1
        for index in range(X.shape[1]):
            values = np.unique(X[:, index])
            for value in values:
                X_left, X_right, y_left, y_right = self._split(X, y, index, value)
                if len(y_left) == 0 or len(y_right) == 0:
                    continue
                gain = self._information_gain(y, y_left, y_right)
                if gain > best_gain:
                    best_index, best_value, best_gain = index, value, gain
        return best_index, best_value

    def _build_tree(self, X, y, depth=0):
        num_samples_per_class = [np.sum(y == i) for i in np.unique(y)]
        predicted_class = np.argmax(num_samples_per_class)
        node = {
            'predicted_class': predicted_class
        }

        if depth < self.max_depth:
            index, value = self._best_split(X, y)
            if index is not None:
                X_left, X_right, y_left, y_right = self._split(X, y, index, value)
                node['index'] = index
                node['value'] = value
                node['left'] = self._build_tree(X_left, y_left, depth + 1)
                node['right'] = self._build_tree(X_right, y_right, depth + 1)
        return node

    def _predict(self, inputs):
        node = self.tree
        while 'index' in node:
            if inputs[node['index']] < node['value']:
                node = node['left']
            else:
                node = node['right']
        return node['predicted_class']


# Example usage:
if __name__ == "__main__":
    # Toy dataset: X (features), y (labels)
    X = np.array([[2.771244718, 1.784783929],
                  [1.728571309, 1.169761413],
                  [3.678319846, 2.81281357],
                  [3.961043357, 2.61995032],
                  [2.999208922, 2.209014212],
                  [7.497545867, 3.162953546],
                  [9.00220326, 3.339047188],
                  [7.444542326, 0.476683375],
                  [10.12493903, 3.234550982],
                  [6.642287351, 3.319983761]])
    y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    # Train decision tree
    clf = DecisionTree(max_depth=3)
    clf.fit(X, y)

    # Make predictions
    predictions = clf.predict(X)
    print("Predictions:", predictions)
