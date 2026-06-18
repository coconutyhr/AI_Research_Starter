import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)

    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    predicted_class = model.predict(new_flower)[0]
    predicted_name = iris.target_names[predicted_class]

    print("Feature names:")
    print(iris.feature_names)

    print("Target names:")
    print(iris.target_names)

    print("Training data size:", len(X_train))
    print("Testing data size:", len(X_test))

    print("First 10 predictions:")
    print(predictions[:10])

    print("First 10 actual labels:")
    print(y_test[:10])

    print("Accuracy:", round(accuracy, 2))

    print("Confusion matrix:")
    print(matrix)

    print("New flower features:")
    print(new_flower[0])

    print("Predicted class:")
    print(predicted_name)

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=iris.target_names
    )
    display.plot()
    plt.title("Iris Classification Confusion Matrix")
    plt.tight_layout()
    plt.savefig("outputs/iris_confusion_matrix.png")

    with open("outputs/iris_classification_report.txt", "w", encoding="utf-8") as file:
        file.write("Iris Classification Report\n")
        file.write("==========================\n")
        file.write(f"Model: KNeighborsClassifier(n_neighbors=3)\n")
        file.write(f"Training data size: {len(X_train)}\n")
        file.write(f"Testing data size: {len(X_test)}\n")
        file.write(f"Accuracy: {round(accuracy, 2)}\n")
        file.write("\nTarget names:\n")
        for index, name in enumerate(iris.target_names):
            file.write(f"{index}: {name}\n")
        file.write("\nConfusion matrix:\n")
        file.write(str(matrix))
        file.write("\n\nNew flower prediction:\n")
        file.write(f"Features: {new_flower[0]}\n")
        file.write(f"Predicted class: {predicted_name}\n")


if __name__ == "__main__":
    main()
