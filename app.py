import streamlit as st
import pickle
import pandas as pd
import requests

# Load the movie dictionary and similarity matrix
try:
    movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_list)
except Exception as e:
    st.error(f"Error loading movie_dict.pkl: {e}")

try:
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading similarity.pkl: {e}")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e2a6e1698f8934f2de85aedf29e3e2b4&language=en-US"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return "https://via.placeholder.com/500x750.png?text=No+Image+Available"  # Placeholder image

    data = response.json()

    # Check if 'poster_path' exists in the response
    if 'poster_path' in data and data['poster_path'] is not None:
        full_path = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    else:
        st.warning("Poster not found for this movie.")
        full_path = "https://via.placeholder.com/500x750.png?text=No+Image+Available"  # Placeholder image

    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

# Streamlit UI setup
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Which movie did you liked the most?', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
