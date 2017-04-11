"""Restaurant rating lister."""


# put your code here
import random

ratings = {}

def make_ratings(file_name):
    """Reads restaurant ratings from file, prints restaurants and score in alphabetical order"""
    restaurant_file = open(file_name)
    for restaurant in restaurant_file:
        restaurant = restaurant.rstrip().split(":")
        name, score = restaurant[0], restaurant[1]
        ratings[name] = score

    restaurant_file.close()


def print_ratings(ratings):
    sorted_ratings = sorted(ratings.items())
    for restaurant, score in sorted_ratings:
        print "%s is rated at %s." % (restaurant, score)


def add_ratings(ratings):
    """Prompt user to add restaurant and rating"""
    while True:
        new_restaurant = raw_input("Enter restaurant name: ")
        new_score = raw_input("Enter score for restaurant: ")
        if int(new_score) < 1 or int(new_score) > 5:
            print "Enter a score between 1 and 5!"
            continue
        else:
            ratings[new_restaurant] = new_score
            break


def random_update(ratings):
    """Returns random restaurant"""
    update = random.choice(ratings.keys())
    print "Please enter updated rating for restaurant %s: " % (update)
    new_rating = raw_input()
    ratings[update] = new_rating
    return

def chosen_update(ratings):
    """Returns chosen restaurant"""
    chosen_restaurant = raw_input("Enter restaurant name: ")
    chosen_rating = raw_input("Enter restaurant score: ")
    ratings[chosen_restaurant] = chosen_rating
    return

def make_choice():
    """Gives user choice between seeing all ratings, adding new restaurant and score, or quitting"""
    print "What would you like to do? "
    print "A: See all the ratings"
    print "B: Add new restaurant and score"
    print "C: Update random restaurant's score"
    print "D: Update restaurant of your choice"
    print "To quit, enter any other letter."
    user_choice = raw_input()

    if user_choice == "A":
        print_ratings(ratings)
        make_choice()
    elif user_choice == "B":
        add_ratings(ratings)
        print_ratings(ratings)
        make_choice()
    elif user_choice == "C":
        random_update(ratings)
        make_choice()
    elif user_choice == "D":
        chosen_update(ratings)
        make_choice()
    else:
        return


make_ratings("scores.txt")
make_choice()
