import pandas as pd


def main():
    df = pd.read_csv("data/students.csv")

    average_score = df["score"].mean()
    highest_score = df["score"].max()
    lowest_score = df["score"].min()

    top_student = df.loc[df["score"].idxmax(), "name"]
    bottom_student = df.loc[df["score"].idxmin(), "name"]

    ranking = df.sort_values(by="score", ascending=False).reset_index(drop=True)
    ranking["rank"] = range(1, len(ranking) + 1)

    print(df)
    print("Average score:", average_score)
    print("Highest score:", highest_score)
    print("Top student:", top_student)
    print("Lowest score:", lowest_score)
    print("Bottom student:", bottom_student)
    print("Ranking:")
    print(ranking[["rank", "name", "score"]])

    ranking[["rank", "name", "score"]].to_csv("outputs/ranking.csv", index=False)


if __name__ == "__main__":
    main()