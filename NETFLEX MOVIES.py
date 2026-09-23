import pandas as pd

df = pd.read_csv("C:\\Users\\dell\\Downloads\\movie.csv")

#For Statical Values
print("Statical Values:",df.describe())
#Most Genre Values
print("Top 10 Genre Moives:\n",df["Genre"].value_counts().head(10))
#Top 10 Movies By Popularity
top_movies = df.sort_values(by="Popularity", ascending=False)
print(top_movies[["Title", "Popularity"]].head(10))
#Visulaise the Top Genre 
import matplotlib.pyplot as plt

genre_count = df["Genre"].value_counts().head(10)
#change the type of chart from KIND if i input BAR in the Kind then it give output
#in the form of Bar Graph
genre_count.plot(kind="line")
#Title is Top 10 Genres
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
# show() use for the Output
plt.show()
#Top rated movie
top_rated = df.sort_values(by="Vote_Average", ascending=False)

print(top_rated[["Title", "Vote_Average"]].head(10))


