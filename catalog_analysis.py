movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

import math


def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]

    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        result = "хорошо" if rating >= 7 and rating <= 8.9 else "шедевр"
        return result
    elif rating >= 5 and rating <= 6.9:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year <= 2020 and year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"
        
def not_comedy(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print("Это не комедия:", movie["title"])

def Best_of_best(movies):
    i = 0

    while i < len(movies):
        movie = movies[i]

        if movie["rating"] > 9.0:
            print(f"Шедевр: {movie['title']}")
            break

        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    c = 0
    for i in movies:
        if i["duration_min"] > threshold:
            c += 1
        else:
            continue
    return c


def normalize_title(title):

    words = title.split()
    result = []
    for word in words:
        new_word = word[0].upper() + word[1:]
        result.append(new_word)

    return " ".join(result)



def make_slug(title):
    words = title.lower().split()
    result = []
    for word in words:
        new_word = word + "-"
        result.append(new_word)

    result[-1] = result[-1].replace("-", "")

    return "".join(result)



def format_report_line(movie):
    time = duration_in_hours(movie["duration_min"])
    return f'"{normalize_title(movie["title"])}" ({movie["year"]}) — {movie["rating"]}/10, {time}, жанры: {", ".join(sorted(movie["genres"]))}'
def titles_sorted_by_rating(movies):
    l = sorted(movies, key=lambda x: x["rating"], reverse=True)

    return [movie["title"] for movie in l]




def top_n_by_rating(movies, n=3):
    l = sorted(movies, key=lambda x: x["rating"], reverse=True)
    r = l[:n]
    result = [(film["title"], film["rating"]) for film in r]
    return result
def count_by_genre(movies):
    result = {}
    for movie in movies:
        genres = movie.get("genres", [])
        for genre in genres:
            result[genre] = result.get(genre, 0) + 1

    return result


def actor_filmography(movies):
    result = {}
    for movie in movies:
        actors = movie.get("actors", [])
        titles = movie.get("title")
        for actor in actors:
            result[actor] = result.get(actor, []) + [titles]

    return result


average_value = average_rating(movies)

high_rated_movies = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_value
}
def all_genres(movies):
    s = set()

    for movie in movies:
        genre = movie.get("genres")
        s.update(genre)
    return s



def common_actors(movie1, movie2):
    s1 = set()
    s2 = set()

    actors1 = movie1.get("actors")
    s1.update(actors1)

    actors2 = movie2.get("actors")
    s2.update(actors2)

    return s1 & s2



def genres_only_in_one(movies_a, movies_b):
    a = set()
    b = set()

    for movie_a in movies_a:
        genre_a = movie_a.get("genres")
        a.update(genre_a)
    for movie_b in movies_b:
        genre_b = movie_b.get("genres")
        b.update(genre_b)

    return a - b
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        movie_rating = movie.get("rating")
        if movie_rating > min_rating:
            yield movie


total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

def build_report(movies):

    average = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")
    top_movies = top_n_by_rating(movies, 3)

    for title, _ in top_movies:
        movie = next(movie for movie in movies if movie["title"] == title)
        print(f"  {format_report_line(movie)}")

    genre_count = count_by_genre(movies)

    sorted_genres = sorted(genre_count.items(), key=lambda item: item[1], reverse=True)

    print("\nФильмов по жанрам:")

    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")

    # Используем all_genres()
    genres = sorted(all_genres(movies))

    result = (f"\nВсе жанры каталога: {', '.join(genres)}")

    return result


if __name__ == "__main__":
    print(build_report(movies))