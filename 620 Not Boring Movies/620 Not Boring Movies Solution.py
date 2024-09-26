import pandas as pd
data = {
    'id': [1, 2, 3, 4, 5],
    'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'],
    'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
    'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
}

cinema = pd.DataFrame(data)
print(cinema)
print(" ")
filtered_cinema = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
result = filtered_cinema.sort_values(by='rating', ascending=False)
print("Answer: ")
print(filtered_cinema)