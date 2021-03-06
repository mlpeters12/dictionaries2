# your code goes here
import sys

def convert_text_to_dict(filename):
    """converting scores.txt into restaurant rating 
    dictionary
    """
    #create empty dictionary
    restaurant_rating = {}

    #open file and loop through data to clean and split data
    for scores_data in open(filename):
        scores_data = scores_data.rstrip().split(":")
        restaurant, rating = scores_data
        
        #checks dictionary for entry, adds restaurant and rating if not already in
        #dictionary

        if restaurant not in restaurant_rating:
            restaurant_rating[restaurant] = int(rating)
           
    return restaurant_rating


def user_adds_rating(restaurant_rating):
    """takes in user input and adds it to restaurant_rating dict"""

    updated_ratings = restaurant_rating
    user_restaurant = raw_input("Let's add your rating! What restaurant do you want to add? ")
    user_rating = raw_input("Rate your restaurant between 1-5, 5 being the best: ")    
    if user_restaurant not in restaurant_rating:
        restaurant_rating[user_restaurant] = int(user_rating)

    return updated_ratings



def sort_restaurant_dict(updated_ratings):
    """sorts restaurant_rating dict and outputs in alphabetized by restaurant string"""

    #create list of tuples of restaurant and rating
    #and returns sorted list by restaurant name
    restaurant_list = sorted(updated_ratings.items())
    
    #loops through sorted restaurant_list to print string
    for restaurant, rating in restaurant_list:
        print " %s is rated at %d." % (restaurant,rating)

restaurant_rating = convert_text_to_dict("scores.txt")
updated_ratings = user_adds_rating(restaurant_rating)
sort_restaurant_dict(updated_ratings)