# Netflix Content Analysis and Visualization

A beginner-friendly data analysis and visualization project using the Netflix Titles dataset. This project uses Python, Pandas, and Matplotlib to clean, analyze, and visualize Netflix content data.

## 📌 Project Overview

The goal of this project is to explore the Netflix dataset and understand patterns such as:

- Number of Movies vs TV Shows
- Distribution of content ratings
- Distribution of movie durations
- Number of titles released by year
- Top countries by number of Netflix titles
- Comparison of Movies and TV Shows released over the years

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib

## 📂 Dataset

The project uses the `netflix_titles.csv` dataset containing information about Netflix Movies and TV Shows.

Important columns used:

- `type`
- `release_year`
- `rating`
- `country`
- `duration`

## 🧹 Data Cleaning

Missing values are removed from important columns using Pandas:

```python
df = df.dropna(
    subset=['type', 'release_year', 'rating', 'country', 'duration']
)
