import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=281a877ed0d0f0b89c554f9d25e0ad3a&language=en-US")
    data=response.json()
    # st.text(data)
    poster_look="https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return poster_look
def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie=[]
    recommend_movie_poster=[]
    for i in movies_list:

        movie_id=movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)

        # Fetch poster id
        recommend_movie_poster.append(fetch_poster(movie_id))
    return recommend_movie

movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)


similarity1 = pickle.load(open('part1_similarity.pkl','rb'))
similarity2 = pickle.load(open('part2_similarity.pkl','rb'))
similarity = similarity1 + similarity2

st.title('Movie - Recommander - System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    (movies['title'].values))

if st.button('Recommend'):
    st.header("I have recommend movie for you!")
    movie_name=recommend(selected_movie_name)
    for i in movie_name:
        st.write(i)


# if st.button('Recommend'):
#     names= recommend(selected_movie_name)
#     poster = recommend(selected_movie_name)
#     col1, col2, col3 , col4 ,col5  = st.columns(5)
#
#     with col1:
#         st.header(names[0])
#         st.image(poster[0])
#     with col2:
#         st.header(names[1])
#         # st.image(poster[1])
#     with col3:
#         st.header(names[2])
#         # st.image(poster[2])
#     with col4:
#         st.header(names[3])
#         # st.image(poster[3])
#     with col5:
#         st.header(names[4])
#         # st.image(poster[4])


