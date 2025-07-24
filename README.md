#  Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit. Select a movie, and it will suggest 5 similar ones based on movie metadata.

<img width="1443" height="859" alt="image" src="https://github.com/user-attachments/assets/be3d5aae-f40c-4600-99ab-4e284ba10348" />


---
 [Live App](https://tanishakathpal-movie-recommendation-app-dlv6qw.streamlit.app)

##  Features

-  Recommends 5 similar movies based on your selection  
-  Fast suggestions using a precomputed similarity matrix  
-  Clean, modern UI with Streamlit  
-  Built using content-based filtering (metadata similarity)

---

##  Project Structure
Movie_Recommendation/

├── app.py # Streamlit app

├── movies.pkl # Movie data

├── similarity.pkl # Precomputed similarity matrix (compressed)

├── requirements.txt # Python dependencies

└── README.md # Project description


---


## Tech Stack

- Python
- Pandas, Scikit-learn
- Streamlit
- Pickle for model storage

##  How It Works

1. Dataset of movies and metadata processed using pandas
2. Similarity scores calculated using cosine similarity
3. When a user selects a movie, top 5 matches are recommended


## Future Enhancements
Poster Fetching By API





