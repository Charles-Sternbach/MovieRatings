# -*- coding: utf-8 -*-
"""
Purpose:
Develop a script that will filter movies from best to worst rating based on
user entered criteria.

@author: Charles Sternbach
"""

import json


def get_input_1():
    """Prompt the user to enter input for the program.

    Prompt the user to enter inclusive upper and lower bounds to determine
    the year range to search through. IMDB weight (w1) and Twitter rating
    weight (w2) are taken from the user to determine which ratings will be
    valued more.

    Returns:
        tuple: Tuple containing 2 integers and 2 floats, the movie year ranges,
        and the weights for w1 and w2.
    """
    min_year = int(input('Min year => '))
    print(min_year)
    max_year = int(input('Max year => '))
    print(max_year)
    w1 = get_number(input('Weight for IMDB => '))
    print(w1)
    w2 = get_number(input('Weight for Twitter => '))
    print(w2)

    return min_year, max_year, w1, w2
    # return 2000, 2016, 0.7, 0.3


def get_input_2():
    """Prompts the user to enter a genre type of interest.

    Returns:
        string: A string containing the genre type.
    """
    user_inputed_genre = input('\nWhat genre do you want to see? ')
    user_inputed_genre_lower = user_inputed_genre.lower()
    if user_inputed_genre_lower == 'stop':
        print("%s\n" % (user_inputed_genre), end='')
    else:
        print("%s\n" % (user_inputed_genre))
    return user_inputed_genre_lower


def finding_movies(movies, ratings, min_year, max_year, w1, w2, user_inputed_genre):
    """Computes and displays the best and worst movies and their respective ratings.

    First, filter movies using the specified year range. Second, filter movies
    by the desired genre type. Third exclude any movie with fewer than three
    Twitter ratings. Add all filtered movie keys into our selected movies list.
    (The value is information about the movie)

    Walk through all the movies into the filtered list to compute the best
    and worst movies. Display this information to the user.

    Args:
        movies: Python dictionary with movie ids as keys and a second
            dictionary containing an attribute list for the movie as a value.
        ratings: Python dictionary with movie ids as keys and a list of Twitter
            ratings as values.
        min_year: Int value representing inclusive lower bound for the
            year range.
        max_year: Int value representing inclusive upper bound for the
            year range.
        w1: float value representing the weight given to IMDB ratings when
            calculating the combined movie rating.
        w2: float value representing the weight given to Twitter ratings when
         calculating the combined movie rating.
        user_inputed_genre: A string containing the genre used to filter movies.
    """
    movies_keys = sorted(movies.keys())

    # Apply filters, and store the selected_movie ids.
    selected_movies = []
    for movie_key in movies_keys:
        dict_movie = movies[movie_key]
        movie_year = dict_movie['movie_year']
        if (movie_year >= min_year and movie_year <= max_year):
            movie_rating = dict_movie['rating']
            # Filter out movies that are in selected genre type.
            if user_inputed_genre in convert_list_to_lower_case(dict_movie['genre']):
                if ratings.get(movie_key):
                    if len(ratings.get(movie_key)) >= 3:
                        selected_movies.append(movie_key)

    if len(selected_movies) == 0:
        print("No %s movie found in %s through %s" % (user_inputed_genre.title(), min_year, max_year))
        return

    # Go through each selected movie, and find the best and worst.
    combined_ratings_list = []
    for movie in selected_movies:
        average_twitter_rating = get_average_rating(ratings[movie])
        dict_movie = movies[movie]
        movie_rating = dict_movie['rating']
        # Formula to compute the combined rating for each movie.
        combined_rating = ((w1 * movie_rating) + (w2 * average_twitter_rating)) / (w1 + w2)
        combined_ratings_list.append((combined_rating, movie))

    sorted_combined_ratings_list = sorted(combined_ratings_list)
    worst_average_rate = sorted_combined_ratings_list[0][0]
    worst_movie = sorted(combined_ratings_list)[0][1]

    best_average_rate = sorted_combined_ratings_list[-1][0]
    best_movie = sorted(combined_ratings_list)[-1][1]

    print("Best:")
    dict_movie = movies[best_movie]
    print("        Released in %s, %s has a rating of %0.2f\n" %
          (dict_movie['movie_year'], dict_movie['name'], best_average_rate))

    print("Worst:")
    dict_movie = movies[worst_movie]
    print("        Released in %s, %s has a rating of %0.2f" %
          (dict_movie['movie_year'], dict_movie['name'], worst_average_rate))


def get_number(number):
    """Convert input value into a integer or a float.

    Args:
        number: String containing weight value provided by the user.

    Returns:
        An integer or a float value based on parsed input.
    """
    if number.isdigit():
        number = int(number)
    else:
        number = float(number)
    return number


def get_average_rating(list1):
    """Compute the average Twitter rating for the given movie id.

    Args:
        list1: A list containing movie ratings for a single movie.

    Returns:
        float: The average Twitter rating for a single movie.
    """
    sum_of_ratings = 0
    num_of_ratings = 0

    for rating in list1:
        sum_of_ratings += rating
        num_of_ratings += 1

    return (sum_of_ratings / num_of_ratings)


def convert_list_to_lower_case(list1):
    """Read in a list containing genre types and convert them to lowercase.

    Args:
        list1: A list containing genre types for a single movie.

    Returns:
        list: A list containing genre types in lowercase.
    """
    for i in range(len(list1)):
        list1[i] = list1[i].lower()
    return (list1)


if __name__ == "__main__":
    # Read in JSON files containing movie ratings.
    movies = json.loads(open("support_files/movies.json").read())
    ratings = json.loads(open("support_files/ratings.json").read())

    # Read in input from user.
    min_year, max_year, w1, w2 = get_input_1()
    user_inputed_genre = get_input_2()

    # Keep asking the user to select a genre type for the given year range.
    # Keep printing out the best and worst movies.
    while user_inputed_genre != "stop":
        finding_movies(movies, ratings, min_year, max_year, w1, w2, user_inputed_genre)
        user_inputed_genre = get_input_2()