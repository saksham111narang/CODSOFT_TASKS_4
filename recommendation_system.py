
# ============================================================
# CODSOFT - TASK 4
# SMART MOVIE RECOMMENDATION SYSTEM
# ============================================================

import math
import re
from difflib import get_close_matches


# ============================================================
# MOVIE DATABASE
# ============================================================

movies = [
    {
        "title": "Inception",
        "genre": "sci-fi thriller action",
        "director": "christopher nolan",
        "keywords": "dream technology mind heist subconscious",
        "rating": 8.8
    },
    {
        "title": "Interstellar",
        "genre": "sci-fi drama adventure",
        "director": "christopher nolan",
        "keywords": "space time travel science future survival",
        "rating": 8.7
    },
    {
        "title": "The Dark Knight",
        "genre": "action crime drama thriller",
        "director": "christopher nolan",
        "keywords": "batman joker hero crime city villain",
        "rating": 9.0
    },
    {
        "title": "The Prestige",
        "genre": "drama mystery thriller",
        "director": "christopher nolan",
        "keywords": "magic rivalry mystery illusion obsession",
        "rating": 8.5
    },
    {
        "title": "Dunkirk",
        "genre": "war drama history thriller",
        "director": "christopher nolan",
        "keywords": "war soldiers survival evacuation military",
        "rating": 7.8
    },
    {
        "title": "Tenet",
        "genre": "sci-fi action thriller",
        "director": "christopher nolan",
        "keywords": "time action espionage technology inversion",
        "rating": 7.3
    },
    {
        "title": "The Matrix",
        "genre": "sci-fi action thriller",
        "director": "lana wachowski",
        "keywords": "virtual reality technology computer future artificial intelligence",
        "rating": 8.7
    },
    {
        "title": "Avatar",
        "genre": "sci-fi action adventure fantasy",
        "director": "james cameron",
        "keywords": "alien planet nature technology adventure pandora",
        "rating": 7.8
    },
    {
        "title": "Titanic",
        "genre": "romance drama history",
        "director": "james cameron",
        "keywords": "love ship ocean tragedy relationship survival",
        "rating": 7.9
    },
    {
        "title": "The Avengers",
        "genre": "action adventure sci-fi",
        "director": "joss whedon",
        "keywords": "superhero marvel team alien battle hero",
        "rating": 8.0
    },
    {
        "title": "Iron Man",
        "genre": "action adventure sci-fi",
        "director": "jon favreau",
        "keywords": "superhero technology marvel robot inventor",
        "rating": 7.9
    },
    {
        "title": "Avengers Endgame",
        "genre": "action adventure sci-fi",
        "director": "anthony russo joe russo",
        "keywords": "superhero marvel time travel team battle infinity",
        "rating": 8.4
    },
    {
        "title": "Spider-Man No Way Home",
        "genre": "action adventure sci-fi fantasy",
        "director": "jon watts",
        "keywords": "superhero marvel multiverse spider man villains",
        "rating": 8.2
    },
    {
        "title": "Guardians of the Galaxy",
        "genre": "action adventure sci-fi comedy",
        "director": "james gunn",
        "keywords": "superhero space marvel team alien galaxy",
        "rating": 8.0
    },
    {
        "title": "Black Panther",
        "genre": "action adventure sci-fi",
        "director": "ryan coogler",
        "keywords": "superhero marvel africa wakanda technology king",
        "rating": 7.3
    },
    {
        "title": "Jurassic Park",
        "genre": "sci-fi adventure thriller",
        "director": "steven spielberg",
        "keywords": "dinosaurs science island adventure survival park",
        "rating": 8.2
    },
    {
        "title": "The Lord of the Rings",
        "genre": "fantasy adventure drama",
        "director": "peter jackson",
        "keywords": "fantasy ring magic war friendship journey middle earth",
        "rating": 8.9
    },
    {
        "title": "Harry Potter",
        "genre": "fantasy adventure family",
        "director": "chris columbus",
        "keywords": "magic wizard school friendship adventure hogwarts",
        "rating": 7.6
    },
    {
        "title": "The Hunger Games",
        "genre": "sci-fi action drama",
        "director": "gary ross",
        "keywords": "survival competition dystopia rebellion future",
        "rating": 7.2
    },
    {
        "title": "Mad Max Fury Road",
        "genre": "action adventure sci-fi",
        "director": "george miller",
        "keywords": "survival desert chase war future vehicles",
        "rating": 8.1
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "drama",
        "director": "frank darabont",
        "keywords": "prison friendship hope freedom survival redemption",
        "rating": 9.3
    },
    {
        "title": "Forrest Gump",
        "genre": "drama romance comedy",
        "director": "robert zemeckis",
        "keywords": "life friendship love history journey hope",
        "rating": 8.8
    },
    {
        "title": "The Godfather",
        "genre": "crime drama",
        "director": "francis ford coppola",
        "keywords": "mafia family crime power business loyalty",
        "rating": 9.2
    },
    {
        "title": "Goodfellas",
        "genre": "crime drama biography",
        "director": "martin scorsese",
        "keywords": "mafia gangster crime family violence money",
        "rating": 8.7
    },
    {
        "title": "The Wolf of Wall Street",
        "genre": "crime comedy drama biography",
        "director": "martin scorsese",
        "keywords": "money business finance fraud wealth stock market",
        "rating": 8.2
    },
    {
        "title": "Gladiator",
        "genre": "action drama history adventure",
        "director": "ridley scott",
        "keywords": "war roman empire revenge warrior battle",
        "rating": 8.5
    },
    {
        "title": "The Martian",
        "genre": "sci-fi drama adventure",
        "director": "ridley scott",
        "keywords": "space mars science survival astronaut technology",
        "rating": 8.0
    },
    {
        "title": "Gravity",
        "genre": "sci-fi drama thriller",
        "director": "alfonso cuaron",
        "keywords": "space astronaut survival technology isolation",
        "rating": 7.7
    },
    {
        "title": "A Beautiful Mind",
        "genre": "drama biography romance",
        "director": "ron howard",
        "keywords": "mathematics genius university friendship achievement",
        "rating": 8.2
    },
    {
        "title": "The Social Network",
        "genre": "drama biography",
        "director": "david fincher",
        "keywords": "technology business friendship programming startup social media",
        "rating": 7.8
    },
    {
        "title": "Fight Club",
        "genre": "drama thriller",
        "director": "david fincher",
        "keywords": "psychology identity rebellion mystery society",
        "rating": 8.8
    },
    {
        "title": "Se7en",
        "genre": "crime mystery thriller",
        "director": "david fincher",
        "keywords": "detective murder mystery crime investigation serial killer",
        "rating": 8.6
    }
]


# ============================================================
# TEXT PROCESSING
# ============================================================

def tokenize(text):
    """
    Converts text into lowercase words.
    """

    return re.findall(r"[a-z]+", text.lower())


def create_feature_text(movie):
    """
    Creates a combined feature string.

    Genre is repeated to give genre more importance.
    """

    return (
        movie["genre"] + " " +
        movie["genre"] + " " +
        movie["director"] + " " +
        movie["keywords"]
    )


# ============================================================
# BUILD VOCABULARY
# ============================================================

def build_vocabulary():

    vocabulary = set()

    for movie in movies:

        words = tokenize(
            create_feature_text(movie)
        )

        vocabulary.update(words)

    return sorted(vocabulary)


# ============================================================
# TERM FREQUENCY
# ============================================================

def term_frequency(words, vocabulary):

    total_words = len(words)

    if total_words == 0:
        return [0] * len(vocabulary)

    vector = []

    for word in vocabulary:

        count = words.count(word)

        vector.append(count / total_words)

    return vector


# ============================================================
# INVERSE DOCUMENT FREQUENCY
# ============================================================

def inverse_document_frequency(vocabulary):

    total_documents = len(movies)

    idf_values = []

    for word in vocabulary:

        documents_containing_word = 0

        for movie in movies:

            words = tokenize(
                create_feature_text(movie)
            )

            if word in words:
                documents_containing_word += 1

        idf = math.log(
            (total_documents + 1) /
            (documents_containing_word + 1)
        ) + 1

        idf_values.append(idf)

    return idf_values


# ============================================================
# TF-IDF VECTOR
# ============================================================

def create_tfidf_vector(movie, vocabulary, idf_values):

    words = tokenize(
        create_feature_text(movie)
    )

    tf_values = term_frequency(
        words,
        vocabulary
    )

    tfidf_vector = []

    for tf, idf in zip(
        tf_values,
        idf_values
    ):

        tfidf_vector.append(tf * idf)

    return tfidf_vector


# ============================================================
# COSINE SIMILARITY
# ============================================================

def cosine_similarity(vector_a, vector_b):

    dot_product = 0
    magnitude_a = 0
    magnitude_b = 0

    for a, b in zip(
        vector_a,
        vector_b
    ):

        dot_product += a * b

        magnitude_a += a * a

        magnitude_b += b * b

    magnitude_a = math.sqrt(magnitude_a)

    magnitude_b = math.sqrt(magnitude_b)

    if magnitude_a == 0 or magnitude_b == 0:

        return 0

    return (
        dot_product /
        (magnitude_a * magnitude_b)
    )


# ============================================================
# FIND MOVIE
# ============================================================

def find_movie(movie_name):

    movie_name = movie_name.lower().strip()

    # Exact match
    for movie in movies:

        if movie["title"].lower() == movie_name:

            return movie

    # Partial match
    for movie in movies:

        if movie_name in movie["title"].lower():

            return movie

    # Fuzzy match
    titles = [
        movie["title"]
        for movie in movies
    ]

    matches = get_close_matches(
        movie_name,
        [title.lower() for title in titles],
        n=1,
        cutoff=0.5
    )

    if matches:

        matched_title = matches[0]

        for movie in movies:

            if movie["title"].lower() == matched_title:

                return movie

    return None


# ============================================================
# GENRE SIMILARITY
# ============================================================

def genre_similarity(movie_a, movie_b):

    genres_a = set(
        tokenize(movie_a["genre"])
    )

    genres_b = set(
        tokenize(movie_b["genre"])
    )

    if not genres_a or not genres_b:

        return 0

    intersection = genres_a.intersection(
        genres_b
    )

    union = genres_a.union(
        genres_b
    )

    return len(intersection) / len(union)


# ============================================================
# DIRECTOR MATCH
# ============================================================

def director_similarity(movie_a, movie_b):

    if movie_a["director"] == movie_b["director"]:

        return 1

    return 0


# ============================================================
# RECOMMENDATION ENGINE
# ============================================================

def recommend_movies(
    movie_name,
    number_of_recommendations=5,
    preferred_genre=None
):

    selected_movie = find_movie(movie_name)

    if selected_movie is None:

        return None

    vocabulary = build_vocabulary()

    idf_values = inverse_document_frequency(
        vocabulary
    )

    selected_vector = create_tfidf_vector(
        selected_movie,
        vocabulary,
        idf_values
    )

    recommendations = []

    for movie in movies:

        if movie["title"] == selected_movie["title"]:

            continue

        movie_vector = create_tfidf_vector(
            movie,
            vocabulary,
            idf_values
        )

        content_score = cosine_similarity(
            selected_vector,
            movie_vector
        )

        genre_score = genre_similarity(
            selected_movie,
            movie
        )

        director_score = director_similarity(
            selected_movie,
            movie
        )

        # Optional user genre preference
        preference_score = 0

        if preferred_genre:

            movie_genres = tokenize(
                movie["genre"]
            )

            if preferred_genre.lower() in movie_genres:

                preference_score = 1

        # Final weighted score
        final_score = (
            content_score * 0.55 +
            genre_score * 0.20 +
            director_score * 0.15 +
            preference_score * 0.10
        )

        recommendations.append(
            {
                "movie": movie,
                "content_score": content_score,
                "genre_score": genre_score,
                "director_score": director_score,
                "preference_score": preference_score,
                "final_score": final_score
            }
        )

    recommendations.sort(
        key=lambda item: item["final_score"],
        reverse=True
    )

    return recommendations[
        :number_of_recommendations
    ]


# ============================================================
# DISPLAY MOVIE LIST
# ============================================================

def display_movies():

    print("\n" + "=" * 60)
    print("AVAILABLE MOVIES")
    print("=" * 60)

    for index, movie in enumerate(
        movies,
        start=1
    ):

        print(
            f"{index:2}. "
            f"{movie['title']} "
            f"⭐ {movie['rating']}"
        )

    print("=" * 60)


# ============================================================
# DISPLAY MOVIE DETAILS
# ============================================================

def show_movie_details(movie_name):

    movie = find_movie(movie_name)

    if movie is None:

        print("\n❌ Movie not found.")

        return

    print("\n" + "=" * 60)
    print("MOVIE DETAILS")
    print("=" * 60)

    print(f"Title    : {movie['title']}")
    print(f"Genre    : {movie['genre'].title()}")
    print(f"Director : {movie['director'].title()}")
    print(f"Rating   : ⭐ {movie['rating']}")
    print(f"Keywords : {movie['keywords']}")

    print("=" * 60)


# ============================================================
# DISPLAY RECOMMENDATIONS
# ============================================================

def display_recommendations(
    movie_name,
    preferred_genre=None
):

    recommendations = recommend_movies(
        movie_name,
        number_of_recommendations=5,
        preferred_genre=preferred_genre
    )

    if recommendations is None:

        print("\n❌ Movie not found.")

        print(
            "Please check the movie name "
            "and try again."
        )

        return

    selected_movie = find_movie(
        movie_name
    )

    print("\n" + "=" * 65)

    print(
        f"🎬 RECOMMENDATIONS FOR: "
        f"{selected_movie['title']}"
    )

    print("=" * 65)

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        movie = recommendation["movie"]

        score = (
            recommendation["final_score"] * 100
        )

        print(
            f"\n{index}. {movie['title']}"
        )

        print(
            f"   ⭐ Rating: {movie['rating']}"
        )

        print(
            f"   🎭 Genre: "
            f"{movie['genre'].title()}"
        )

        print(
            f"   🎬 Director: "
            f"{movie['director'].title()}"
        )

        print(
            f"   📊 Recommendation Score: "
            f"{score:.2f}%"
        )

        # Explanation
        reasons = []

        if recommendation[
            "genre_score"
        ] > 0:

            reasons.append(
                "similar genre"
            )

        if recommendation[
            "director_score"
        ] > 0:

            reasons.append(
                "same director"
            )

        if recommendation[
            "content_score"
        ] > 0.15:

            reasons.append(
                "similar keywords"
            )

        if recommendation[
            "preference_score"
        ] > 0:

            reasons.append(
                "matches your preferred genre"
            )

        if reasons:

            print(
                "   💡 Why recommended: "
                + ", ".join(reasons)
            )

    print("\n" + "=" * 65)


# ============================================================
# GET GENRE PREFERENCE
# ============================================================

def get_genre_preference():

    print("\nOptional Genre Preference")

    print(
        "Examples: action, drama, sci-fi, "
        "romance, comedy"
    )

    genre = input(
        "Enter preferred genre "
        "(or press Enter to skip): "
    ).strip().lower()

    if genre == "":

        return None

    return genre


# ============================================================
# MAIN MENU
# ============================================================

def main():

    print("=" * 65)
    print("       SMART MOVIE RECOMMENDATION SYSTEM")
    print("                CODSOFT TASK 4")
    print("=" * 65)

    print(
        "\n🧠 Recommendation Method:"
    )

    print(
        "Content-Based Filtering + "
        "TF-IDF + Cosine Similarity"
    )

    while True:

        print("\n" + "-" * 50)

        print("MAIN MENU")

        print("-" * 50)

        print("1. View all movies")

        print("2. Get recommendations")

        print("3. View movie details")

        print("4. Exit")

        print("-" * 50)

        choice = input(
            "Enter your choice (1-4): "
        ).strip()

        # ------------------------------------------------
        # OPTION 1
        # ------------------------------------------------

        if choice == "1":

            display_movies()

        # ------------------------------------------------
        # OPTION 2
        # ------------------------------------------------

        elif choice == "2":

            display_movies()

            movie_name = input(
                "\n🎬 Enter a movie you like: "
            ).strip()

            preferred_genre = (
                get_genre_preference()
            )

            display_recommendations(
                movie_name,
                preferred_genre
            )

        # ------------------------------------------------
        # OPTION 3
        # ------------------------------------------------

        elif choice == "3":

            movie_name = input(
                "\nEnter movie name: "
            ).strip()

            show_movie_details(
                movie_name
            )

        # ------------------------------------------------
        # OPTION 4
        # ------------------------------------------------

        elif choice == "4":

            print("\n" + "=" * 50)

            print(
                "Thank you for using the "
                "Smart Movie Recommendation System! 🎬"
            )

            print(
                "Keep watching. Keep discovering. 🍿"
            )

            print("=" * 50)

            break

        # ------------------------------------------------
        # INVALID INPUT
        # ------------------------------------------------

        else:

            print(
                "\n❌ Invalid choice."
            )

            print(
                "Please select an option "
                "between 1 and 4."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()