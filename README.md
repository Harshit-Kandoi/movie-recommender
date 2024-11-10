# Movie Recommender System

A machine learning-based movie recommendation system that suggests similar movies based on user preferences. This project uses a content-based filtering approach, analyzing factors like genres, keywords, cast, and crew to recommend movies.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Model Overview](#model-overview)
- [Data](#data)
- [Acknowledgments](#acknowledgments)

## Features

- **Movie Recommendations**: Enter a movie title, and get recommendations based on similar attributes.
- **Interactive Web Interface**: Easy-to-use Streamlit app for user interaction.
- **Content-Based Filtering**: Recommendations rely on the content of each movie, making it ideal for new or less popular movies.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Harshit-Kandoi/movie-recommender.git
   ```

2. **Navigate to Project Directory**:
   ```bash
   cd movie-recommender
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Running the App**:
   Start the recommendation system using Streamlit by running:
   ```bash
   streamlit run app.py
   ```

2. **Using the Jupyter Notebook**:
   For exploring or modifying the recommendation model, open `movie.ipynb` in Jupyter Notebook.

3. **Input Movie Title**:
   In the app, input a movie title, and the system will display similar movies.

## Files

- **app.py**: The main file to launch the Streamlit app.
- **movie.ipynb**: Jupyter notebook for developing and testing the recommendation model.
- **movie_dict.pkl & similarity.pkl**: Pickle files containing data structures for the recommendation system.
- **tmdb_5000_credits.csv & tmdb_5000_movies.csv**: Movie datasets for building the recommendation engine.
- **requirements.txt**: Lists the necessary libraries to run this project.

## Model Overview

This recommender system employs a content-based filtering approach, where cosine similarity is used to measure similarity between movies. Features like genres, cast, crew, and keywords are combined to create a "movie vector," which helps in identifying similar movies.

## Data

The dataset used is sourced from [The Movie Database (TMDb)](https://www.themoviedb.org/), consisting of movie details like genres, cast, crew, and keywords. The processed data is stored in `movie_dict.pkl` and `similarity.pkl`.

## Acknowledgments

- Special thanks to [TMDb](https://www.themoviedb.org/) for the dataset.
- Inspiration and guidance from the open-source community.
