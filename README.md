#  Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit. Select a movie, and it will suggest 5 similar ones based on movie metadata.

<img width="1443" height="859" alt="image" src="https://github.com/user-attachments/assets/be3d5aae-f40c-4600-99ab-4e284ba10348" />


---

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



Movie data is extracted from TMDb and processed using Pandas

A similarity matrix is generated using content features like genres, overview, keywords, etc.

similarity.pkl stores cosine similarity scores between movies

Streamlit UI allows users to select a movie and view recommendations

## Note
Due to TMDb being intermittently blocked in some regions, poster images were not fetched yet. This feature may be added in future updates.






