import numpy as np

def perceptron_algorithm(X, y, learning_rate=0.1, threshold=0.5, max_iterations=100):
    weights = np.zeros(X.shape[1])
    iteration = 0

    while iteration < max_iterations:
        correctly_classified = True

        for i in range(len(X)):
            f = X[i]
            c = y[i]
            o = np.dot(weights, f)
            o = 1 if o >= threshold else 0
            error = learning_rate * (c - o)

            if error != 0:
                correctly_classified = False
                weights = weights + error * f

        iteration += 1

        if correctly_classified:
            break

    predictions = [1 if np.dot(weights, x) >= threshold else 0 for x in X]

    return weights, predictions, iteration


# Example usage
if __name__ == "__main__":
    # Dataset
    data = np.array([
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ])

    X = data[:, :-1]  # Features
    y = data[:, -1]   # Labels

    # Run perceptron
    weights, predictions, iterations = perceptron_algorithm(X, y, learning_rate=0.1, threshold=0.5)

    # Print results
    print("Final Weights:", weights)
    print("Predictions:", predictions)
    print("Number of Iterations:", iterations)