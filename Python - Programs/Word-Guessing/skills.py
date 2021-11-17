import random as rd
import food as fd

# Random Fruits word
def random_fruit():
    point_count = 0
    time_play = 0
    while time_play == 6:
        time_play += 1
        rdf_c = rd.choice(fd.all_food['fruits'])
        print(rdf_c)
        guess1 = input()
        if guess1 == rdf_c:
            print("You guessed right!")
            point_count += 1
            print("Points: " + str(point_count))
        elif guess1 != rdf_c:
            print("Wrong!")
            point_count -= 1
            print("Points: " + str(point_count))
    #rand = rd.choice(rdf_c)
#print(random_fruit())

# Random Vegetables word

# Ask player if it's a vegatable or a fruit


# Random number - easy (1, 10), - medium (1, 50), - hard (1, 100)

while True:
    guess = input("Choose game: ")
    if guess == "H":
        random_fruit()
    else:
        print("Try again!")