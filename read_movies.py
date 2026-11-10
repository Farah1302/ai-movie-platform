
import json

with open("movies.json", "r", encoding="utf-8") as file:
    movie = json.load(file)

print("Movie Information")
print("-----------------")
print(f"ID: {movie['id']}")
print(f"Title: {movie['title']}")
print(f"Year: {movie['year']}")
print(f"Rating: {movie['rating']}")
