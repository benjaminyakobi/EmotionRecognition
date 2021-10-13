import os
import pandas as pd


def search_movie(name):
    """
    receives a string from the user search and returns a dictionary of results:
    {name:id}
    """
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    f = pd.read_csv('Data/Movie_Recommendation/MovieSearch.csv')
    # split the and lowercase words
    name = name.lower()
    name = name.split()
    # parameters for search
    searches = []
    i = 0
    # for each word we will add a column that will have -1 if the string doesnt contain the word and index if it does
    for word in name:
        searches.append(i)
        f[i] = f["title"].str.find(word)
        i += 1
    # filtering all results that don't contain each word
    for item in searches:
        f = f.loc[f[item] > -1]

    result = {}
    i = 0
    # put the id of each movie
    for index, row in f.iterrows():
        result[row['title'] + '(' + str(row['year']) + ')'] = row.id
        i += 1
        if i > 49:
            break

    if len(result) > 0:
        return result
    return 0


def search_movie_id(id):
    f = pd.read_csv('Data/Movie_Recommendation/MovieSearch.csv')
    res=f.loc[f['id']==id]
    return res.iloc[0]['title']


