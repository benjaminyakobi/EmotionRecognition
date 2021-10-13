import numpy as np
import pandas as pd


def get_recommendations(id):
    cosine_sim = np.load('Data/Movie_Recommendation/cosine_sim.npy')
    df = pd.read_csv('Data/Movie_Recommendation/df3.csv')
    print(df[df['id'] == id].index[0])
    # Get the similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[df[df['id'] == id].index[0]]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:10]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies
    return df['title'].iloc[movie_indices]
