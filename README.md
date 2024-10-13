MovieRatings Project
-
Given a year range, two weights w1 and w2, and a genre type, we want to
calculate the best and worst rated movies.

Input from the user:
-
The following input is needed from the user:
1. Minimum Year:

This represents the inclusive lower bound where we begin analyzing movie ratings.

Example Input:
Min year => 2004

2. Maximum Year:

This represents the inclusive upper bound where we stop analyzing movie ratings.

Example Input: Max year => 2012


3. Weight for IMDB (w1)

This is the weight given to IMDB ratings when calculating the combined
movie rating.

Example Input: Weight for IMDB => 0.7

4. Weight for Twitter ratings (w2):

This is the weight given to Twitter ratings when calculating the combined 
movie rating.

5. Genre:
- The program will find the best and worst movies for a particular genre
specified by the user.
- When prompted one fo the following genre types can be given:

Action, Adventure, Animation, Biography, Comedy, Crime, Documentary
Drama, Family, Fantasy, History, Horror, Music, Musical, Mystery, 
Romance, Sci-Fi, Sport, Thriller, War, Western.

Solving the Problem:
-
- For each movie we will compute the combined rating as:

combined_rating = (w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2)

IMDB rating will come from movies.json and average_twitter_rating will come from
ratings.json.

- If the movie is not rated in Twitter, or if the Twitter rating has fewer than
three entries, we skip the movie.

- Finally we will keep asking the user for a genre of movie and return
the best and worst movies until they choose to exit the program.