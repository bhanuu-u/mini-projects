import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
print(df.head())

# cleaning
df = df.dropna(subset=['type','release_year','rating','country','duration'])

# ---------------------------------------------------------------------------------------------
type_counts = df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title("Number of MOVIES VS TV show on netflix")
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig("movies_vs_tvshow.png")
plt.show()

# ---------------------------------------------------------------------------------------------
rating_count = df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct="%1.1f%%",startangle=90)
plt.title("Percentage of content rating")
plt.tight_layout()
plt.savefig("content_ratings.png")
plt.show()
# ---------------------------------------------------------------------------------------------

movie_df = df[df["type"] == "Movie"].copy()
movie_df["duration_int"] = movie_df["duration"].str.replace(" min","").astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df["duration_int"],bins=40,color="skyblue",edgecolor="black")
plt.title("Distribution of movie duration")
plt.xlabel("duration(mins)")
plt.ylabel("Number of movies")
plt.savefig("Distribution_movie_duration",dpi=300)
plt.show()
# ---------------------------------------------------------------------------------------------

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_count.index,release_count.values,color="black")
plt.title("Release year vs number of shows")
plt.xlabel("release year")
plt.ylabel("Number of shows")
plt.savefig("Release year vs number of shows",dpi=300)
plt.show()
# ---------------------------------------------------------------------------------------------
country_counts = df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color = "green")
plt.title("top 10 countries by Number of Shows")
plt.xlabel("Number of shows")
plt.ylabel("country")
plt.savefig("top 10 countries by Number of Shows",dpi=300)
plt.show()

# ---------------------------------------------------------------------------------------------
country_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)

fig,ax = plt.subplots(1,2, figsize=(12,5))

ax[0].plot(country_by_year.index,country_by_year["Movie"],color= "blue")
ax[0].set_title("Movies released per year")
ax[0].set_xlabel("year")
ax[0].set_ylabel("Number of movies")


ax[1].plot(country_by_year.index,country_by_year["TV Show"],color= "blue")
ax[1].set_title("TV show released per year")
ax[1].set_xlabel("year")
ax[1].set_ylabel("Number of TV shows")

fig.suptitle("comparison of movies and tv shows released over years")
plt.tight_layout()
plt.savefig("Comparison of Movies and Tv shows released over years")
plt.show()

# ---------------------------------------------------------------------------------------------