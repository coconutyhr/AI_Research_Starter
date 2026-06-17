import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    df = pd.read_csv("data/study_scores.csv")

    X = df[["study_hours"]]
    y = df["score"]

    model = LinearRegression()
    model.fit(X, y)

    new_data = pd.DataFrame({"study_hours": [9]})
    raw_predicted_score = model.predict(new_data)[0]
    predicted_score = min(raw_predicted_score, 100)

    predicted_line = model.predict(X)

    print(df)
    print("Predicted score for 9 study hours:", predicted_score)

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