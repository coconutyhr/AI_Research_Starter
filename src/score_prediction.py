import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    df = pd.read_csv("data/study_scores.csv")

    X = df[["study_hours"]]
    y = df["score"]

    model = LinearRegression()
    model.fit(X, y)

    new_data = pd.DataFrame({"study_hours": [9]})
    predicted_score = model.predict(new_data)
    predicted_score = min(predicted_score[0], 100)

    print(df)
    print("Predicted score for 9 study hours:", predicted_score)


if __name__ == "__main__":
    main()