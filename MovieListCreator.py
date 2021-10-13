import pandas as pd

# loading only the relevant fields
f = pd.read_csv('Data/Movie_Database/tmdb_5000_movies.csv')
id = f['id']
title = f["original_title"]
release = f["release_date"]

# print(id.head)
# print(title.head)
# print(release.head)

# extracting year from dates
def extract_year(x):
    if isinstance(x, float):
        return 0
    return x[:4]

year = release.apply(extract_year)
# print(year.head)

# change the names to lower case
title = title.apply(str.lower)

# merging columns
df = pd.concat([id, title, year], axis=1)
# print(df.head)


# renaming columns
df.rename(columns={'original_title': 'title', 'release_date': 'year'}, inplace=True)

df.to_csv('Data/Movie_Recommendation/MovieSearch.csv', index=False)
