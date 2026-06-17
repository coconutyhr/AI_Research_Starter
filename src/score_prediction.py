import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def main():
    df = pd.read_csv("data/study_scores.csv")

    X = df[["study_hours"]]
    y = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    test_predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, test_predictions)

    new_data = pd.DataFrame({"study_hours": [9]})
    raw_predicted_score = model.predict(new_data)[0]
    predicted_score = min(raw_predicted_score, 100)

    predicted_line = model.predict(X)

    print("Training features:")
    print(X_train)
    print("Testing features:")
    print(X_test)
    print("Testing predictions:", test_predictions)
    print("Actual testing scores:")
    print(y_test)
    print("Mean absolute error:", round(mae, 2))
    print("Predicted score for 9 study hours:", round(predicted_score, 2))

    plt.figure(figsize=(8, 5))
    plt.scatter(df["study_hours"], df["score"], label="Actual data")
    plt.plot(df["study_hours"], predicted_line, label="Regression line")
    plt.scatter([9], [predicted_score], label="Prediction for 9 hours")
    plt.xlabel("Study hours")
    plt.ylabel("Score")
    plt.title("Study Hours and Exam Score Prediction")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/score_prediction_plot.png")


if __name__ == "__main__":
    main()