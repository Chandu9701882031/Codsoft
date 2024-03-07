import random

# Sample book data (replace with your dataset)
books_data = {
    'book1': ['Author1', 'Genre1'],
    'book2': ['Author2', 'Genre2'],
    'book3': ['Author3', 'Genre3'],
    'book4': ['Author4', 'Genre1'],
    'book5': ['Author5', 'Genre2'],
    'book6': ['Author6', 'Genre3'],
    'book7': ['Author7', 'Genre1'],
    'book8': ['Author8', 'Genre2'],
    'book9': ['Author9', 'Genre3'],
    'book10': ['Author10', 'Genre1']
}

# Sample user preferences (replace with actual user preferences)
user_preferences = ['Genre1', 'Genre2']

# Recommend books based on user preferences
def recommend_books(preferences, num_recommendations=5):
    recommended_books = []
    for book, details in books_data.items():
        if details[1] in preferences:
            recommended_books.append(book)
    random.shuffle(recommended_books)
    return recommended_books[:num_recommendations]

# Get recommended books for the user
recommended_books = recommend_books(user_preferences)

# Print recommended books
print("Recommended books for the user based on their preferences:")
for book in recommended_books:
    print(book)
