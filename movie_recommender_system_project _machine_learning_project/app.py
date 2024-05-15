<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_movie_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a37c29a52daa4dba4c925f5d4168cfb8'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]
    
    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        print(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_poster.append(fetch_movie_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'How would you like to be contected',
    movies['title'].values
)


if st.button('Choose Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, = st.columns(5)
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
=======
import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_movie_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a37c29a52daa4dba4c925f5d4168cfb8'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]
    
    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        print(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_poster.append(fetch_movie_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'How would you like to be contected',
    movies['title'].values
)


if st.button('Choose Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, = st.columns(5)
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
>>>>>>> d379f005809cf741a527ca992e40187f7c6b7fcf
