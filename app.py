import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.markdown("""
    <style>
        .stApp {
            
            background-color: #0f172a;
            color: #e2e8f0;
        }

        .stSelectbox label {
            color: #00ffff;
            font-weight: bold;
            font-size: 16px;
        }

        .stButton>button {
            background-color: #00ffff;
            color: #0f172a;
            padding: 0.75em 1.5em;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            transition: 0.3s ease;
        }

        .stButton>button:hover {
            background-color: gray;
            color: white;
        }

        h1, h3 {
            text-align: center;
        }

        .recommend-title {
            color: #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='recommend-title'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Select a movie and we'll recommend some great ones!</p>", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

selected_movie = st.selectbox("Choose a movie:", movies_list)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_indices]
    return recommended_movies


if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.markdown("### Top Recommendations:")
    for idx, title in enumerate(recommendations, 1):
        st.markdown(f"{idx}. **{title}**")

# poster fetch:future enhancements
