# 📚 Book Recommendation System (Hybrid Filtering)

This project is a **Book Recommendation System** built using a **hybrid filtering** approach, which combines both **popularity-based** and **collaborative filtering** techniques to provide more accurate and personalized book suggestions.

## 🎯 Objective

To recommend books to users based on their interests and past behavior using a mix of similarity-based and rating-based filtering methods.

## 🚀 Features

- Hybrid Recommendation Engine:
  - **Popularity-based Filtering** (based on book popularity)
  - **Collaborative Filtering** (based on user ratings)
- Fast and efficient similarity search using **cosine similarity**
- Interactive web interface using **Streamlit**
- Clean and user-friendly UI
- Lightweight and runs locally

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** (cosine similarity)
- **Streamlit** (for web UI)
- **Pickle** (for saving models and preprocessed data)

## 🧠 How It Works

1. **Data Preprocessing**: Cleaned and structured a dataset of books and user ratings.
2. **Content-Based Filtering**: Recommends books similar to the one the user likes using text similarity.
3. **Collaborative Filtering**: Suggests books based on the behavior of similar users.
4. **Hybrid Filtering**: Combines the strengths of both methods to improve recommendation quality.

5. 
## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/book-recommender.git
cd book-recommender
