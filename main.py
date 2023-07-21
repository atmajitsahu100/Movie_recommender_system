#movie recommender

import streamlit as st
import requests
import pickle

def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bbd5db83255beb7966f303bf5c3ae5c4&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/original" + data['poster_path']
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_lists:
        recommended_movies.append(movies[i[0]])
        recommended_movies_poster.append(fetch_poster(movie_id[i[0]]))
    return recommended_movies, recommended_movies_poster


movies_list = pickle.load(open('movies.pkl','rb'))
movie_id = movies_list['id'].values
movies = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'choose your movie',
    movies)

if st.button('Recommend'):
  names, posters = recommend(selected_movie)

  col1,col2,col3,col4,col5 = st.columns(5)
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