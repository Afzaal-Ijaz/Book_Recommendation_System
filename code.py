
import streamlit as st
import pickle
import numpy as np

# Load data
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))

# Recommend function
def recommend(book_name, top_n):
    try:
        index = np.where(pt.index == book_name)[0][0]
    except IndexError:
        return None  # Book not found

    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:top_n+1]

    data = []
    for i in similar_items:
        temp = books[books['Book-Title'] == pt.index[i[0]]]
        title = temp.drop_duplicates('Book-Title')['Book-Title'].values[0]
        author = temp.drop_duplicates('Book-Title')['Book-Author'].values[0]
        image_url = temp.drop_duplicates('Book-Title')['Image-URL-M'].values[0]
        data.append([title, author, image_url])
    return data

# Streamlit UI
st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 AI-Powered Book Recommendation System")

# Autocomplete dropdown
book_list = pt.index.tolist()
book_input = st.selectbox("🔍 Choose a Book Title", book_list)

# Slider for number of recommendations
top_n = st.slider("📊 Number of Recommendations", min_value=1, max_value=20, value=5)

# Recommend Button
if st.button("✨ Recommend Books"):
    recommendations = recommend(book_input, top_n)
    if recommendations is None:
        st.error("❌ Book not found.")
    else:
        # Show recommendations side-by-side in columns
        num_cols = 3  # number of columns per row
        rows = (len(recommendations) + num_cols - 1) // num_cols
        for row in range(rows):
            cols = st.columns(num_cols)
            for col_idx in range(num_cols):
                idx = row * num_cols + col_idx
                if idx < len(recommendations):
                    book = recommendations[idx]
                    with cols[col_idx]:
                        st.image(book[2], width=150)
                        st.markdown(f"**{book[0]}**")
                        st.markdown(f"👤 *{book[1]}*")
