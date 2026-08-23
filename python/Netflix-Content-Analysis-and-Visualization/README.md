# Netflix Content Analysis and Visualization

A beginner-friendly data analysis and visualization project using the Netflix Titles dataset. This project uses Python, Pandas, and Matplotlib to clean, analyze, and visualize Netflix Movies and TV Shows data.

## 📌 Project Overview

The goal of this project is to explore the Netflix dataset and identify patterns and trends in the available content.

The project analyzes:

- Number of Movies vs TV Shows
- Distribution of content ratings
- Distribution of movie durations
- Number of titles released by year
- Top 10 countries by number of titles
- Comparison of Movies and TV Shows released over the years

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib

## 📂 Dataset

The project uses the `netflix_titles.csv` dataset containing information about Netflix Movies and TV Shows.

The raw CSV dataset is included in this repository so that the analysis can be reproduced.

### Important Columns Used

- `type` — Movie or TV Show
- `release_year` — Year the title was released
- `rating` — Content rating
- `country` — Country associated with the title
- `duration` — Movie duration or number of seasons

## 🧹 Data Cleaning

Missing values are removed from important columns using Pandas:

```python
df = df.dropna(
    subset=['type', 'release_year', 'rating', 'country', 'duration']
)
