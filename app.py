import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ad3b7bd6ce842b600131fe11574a456a&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
     id = movies.iloc[i[0]].id
     recommend_movies.append(movies.iloc[i[0]].title)
     recommend_movies_posters.append(fetch_poster(id))

    return recommend_movies, recommend_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Discover More: If You Enjoyed This, You will Love the Following', movies['title'].values )
if st.button('Recommend'):

    recommend_movie_names, recommend_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movie_names[0])
        st.image(recommend_movie_posters[0])
    with col2:
        st.text(recommend_movie_names[1])
        st.image(recommend_movie_posters[1])

    with col3:
        st.text(recommend_movie_names[2])
        st.image(recommend_movie_posters[2])
    with col4:
        st.text(recommend_movie_names[3])
        st.image(recommend_movie_posters[3])
    with col5:
        st.text(recommend_movie_names[4])
        st.image(recommend_movie_posters[4])





