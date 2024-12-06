import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def identify_features_and_classes(data):
    features = data.columns[:-1]
    data[data.columns[-1]] = data[data.columns[-1]].apply(lambda x: 1 if x == 'M' else 0)
    classes = data[data.columns[-1]].unique()
    return features, classes

def shuffle_and_split_data(data):
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42, shuffle=True)
    return train_data, test_data

def calculate_accuracy(predictions, y):
    correct_predictions = sum(pred == actual for pred, actual in zip(predictions, y))
    accuracy = correct_predictions / len(y)
    return accuracy

def perceptron_algorithm(X, y, learning_rate=0.1, threshold=0.5, max_iterations=100, target_accuracy=0.75):
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
        predictions = [1 if np.dot(weights, x) >= threshold else 0 for x in X]
        accuracy = calculate_accuracy(predictions, y)

        if accuracy >= target_accuracy:
            break

        if correctly_classified:
            break

    return weights, predictions, iteration, accuracy

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

def main():
    file_path = 'sonar.all-data.csv'
    data = read_csv(file_path)
    
    features, classes = identify_features_and_classes(data)
    train_data, test_data = shuffle_and_split_data(data)
    
    X_train = train_data[features].values
    y_train = train_data[data.columns[-1]].values
    X_test = test_data[features].values
    y_test = test_data[data.columns[-1]].values
    
    weights, train_predictions, iterations, train_accuracy = perceptron_algorithm(X_train, y_train)
    
    test_predictions = [1 if np.dot(weights, x) >= 0.5 else 0 for x in X_test]
    
    test_accuracy = calculate_accuracy(test_predictions, y_test)
    
    plot_confusion_matrix(y_test, test_predictions)
    print(f"Training completed in {iterations} iterations with training accuracy: {train_accuracy:.2f}")
    print(f"Testing accuracy: {test_accuracy:.2f}")

if __name__ == "__main__":
    main()
