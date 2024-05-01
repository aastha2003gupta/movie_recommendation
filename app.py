import pickle
import streamlit as st

COLOR_PALETTE = {
    "background": "#1F1F1F",  
    "header": "#61dafb",      
    "button": "#3b5998",      
    "text": "#FFFFFF",        
    "accent": "#FF4081",      
}

st.markdown(
    f"""
    <style>
        body {{
            background: {COLOR_PALETTE["background"]};
            color: {COLOR_PALETTE["text"]};
        }}
        .st-bj {{
            background: {COLOR_PALETTE["header"]};
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            padding: 10px;
        }}
        .st-cg {{
            background: {COLOR_PALETTE["button"]};
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.3s;
        }}
        .st-cg:hover {{
            background: {COLOR_PALETTE["accent"]};
        }}
        .st-ct {{
            color: {COLOR_PALETTE["text"]};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movie_names

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Cinema Nudge')
st.write('Discover similar movies by selecting your favorite!')

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button('Show Recommendations', key='recommend_btn'):
    recommended_movie_names = recommend(selected_movie)

    cols = st.columns(5)

    for i, (col, recommended_movie) in enumerate(zip(cols, recommended_movie_names), 1):
        with col:
            st.markdown(f"{i}. **{recommended_movie}**", unsafe_allow_html=True)

st.markdown(
    """
    ---
    *Developed with ❤️ by Aastha Gupta*
    """,
    unsafe_allow_html=True
)
