# 🎬 CODSOFT TASK 4 — MOVIE RECOMMENDATION SYSTEM

## 📌 About the Project

This project is developed as part of the **CodSoft Artificial Intelligence Internship**.

The project is a **content-based movie recommendation system** developed using Python.

The system recommends movies based on similarities between movie genres, directors, keywords, and user preferences.

It uses **TF-IDF** to represent movie features numerically and **Cosine Similarity** to measure the similarity between movies.

---

## ✨ Features

- 🎬 Movie recommendations
- 🧠 Content-based filtering
- 📊 TF-IDF feature representation
- 📐 Cosine similarity
- 🎭 Genre preference
- 🎥 Director similarity
- ⭐ Movie ratings
- 🔎 Fuzzy movie-name matching
- 📋 Movie details
- 📊 Recommendation scoring
- 🔄 Interactive menu
- ⚠️ Invalid input handling

---

## 🧠 Recommendation Method

The system uses **Content-Based Filtering**.

Instead of relying on other users' ratings, the system compares the characteristics of movies.

The system analyzes:

- Movie genre
- Director
- Keywords
- User's preferred genre

The system then calculates similarity between movies and ranks the most relevant recommendations.

---

## 🔄 Recommendation Process

```text
              User Selects Movie
                     ↓
             Extract Movie Features
                     ↓
          Genre + Director + Keywords
                     ↓
                  TF-IDF
                     ↓
          Numerical Representation
                     ↓
             Cosine Similarity
                     ↓
             Genre Similarity
                     ↓
           Director Similarity
                     ↓
        User Genre Preference
                     ↓
          Final Recommendation Score
                     ↓
             Top Recommendations
