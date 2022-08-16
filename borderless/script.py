"""
Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the
pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a
person’s interests are and then give them recommendations in their area to venues, restaurants, and historical
destinations that we think they’ll be engaged by. Let’s get started!
"""


def get_destination_index(destination):
    """
    This function takes a string (destination) and returns the index position
    """

    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    """
    This method uses traveler_destination along with get_destination_index() to retrieve the index of the
    destination where the traveler is.
    """
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


def add_attraction(destination, attraction):
    """
    This function will add an attraction to a city
    First we should attempt to find the index of the destination. Use get_destination_index()
    with the passed in destination.
    If the destination does exist, then we already have a list for it in attractions. Use the destination_index to find the appropriate
    list in attractions and save that list to attractions_for_destination.
    """
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)  # Append the attraction passed into add_attraction to the list
    # attractions_for_destination

    return attractions_for_destination


def find_attractions(destination, interests):
    """
    We want to be able to help our traveler’s find the most interesting places in a new city for them. In order to
    do that we need to match their interests with the possible locations in a city
    """
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []  # empty list we’ll save attractions into
    # if they match one of our interests

    for item in attractions_in_city:
        possible_attraction = item
        attraction_tags = possible_attraction[1]  # For each attraction, retrieve the tagged information about it.
        # The tags are all saved in the second place (index 1) in the attraction

        # we want to see if any of the given interests are in attraction_tags
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = f"Thank you for your enquiry {traveler[0]}, we think you'll like these places around {traveler[1]}: "

    for item in traveler_attractions:
        interests_string += item + ".\n"

    return interests_string


"""
This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical 
buildings and art. Erin is in China right now.
"""

destinations = ['Paris, France',
                'Shanghai, China',
                'Los Angeles, USA',
                'São Paulo, Brazil',
                'Cairo, Egypt']

test_traveler = ['Erin Wilkes',
                 'Shanghai, China',
                 ['historical site', 'art']
                 ]

# an empty list for every destination in destinations using list comprehension
attractions = [[] for destination in destinations]

# adding more attractions
add_attraction('Los Angeles, USA', ['Venice Beach', 'beach'])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

logged = True

while logged:
    print("Hello, welcome to Bordlerless Traveler\n")

    name = input("Please enter your name: ")
    print(f"Welcome {name}, we cover a few select destinations, please select a destination: ")
    location = int(input("""
    1) Los Angeles USA
    2) Paris, France
    3) Shangai, China
    4) São Paulo, Brazil
    5) Cairo, Egypt
    """))

    # Los Angeles
    if location == 1:
        location = "Los Angeles, USA"
        print(f"What would you like to see in {location}? : ")
        tag = int(input("""
        1) Beach
        2) Museum
        """))

        if tag == 1:
            tag = "beach"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
        elif tag == 2:
            tag = "museum"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()

    # Paris
    elif location == 2:
        location = "Paris, France"
        print(f"What would you like to see in {location}? : ")
        tag = int(input("""
        1) Art
        2) Historical site
        """))

        if tag == 1:
            tag = "art"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
        elif tag == 2:
            tag = "historical site"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()

    # Shanghai
    elif location == 3:
        location = "Shanghai, China"
        print(f"What would you like to see in {location}? : ")
        tag = int(input("""
        1) Museum
        2) Historical site
        """))

        if tag == 1:
            tag = "museum"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
        elif tag == 2:
            tag = "historical site"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()

    # São Paulo
    elif location == 4:
        location = "São Paulo, Brazil"
        print(f"What would you like to see in {location}? : ")
        tag = int(input("""
        1) Zoo
        2) Historical site
        """))

        if tag == 1:
            tag = "zoo"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
        elif tag == 2:
            tag = "historical site"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()

    # São Paulo
    elif location == 5:
        location = "Cairo, Egypt"
        print(f"What would you like to see in {location}? : ")
        tag = int(input("""
        1) Museum
        2) Historical site
        """))

        if tag == 1:
            tag = "museum"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
        elif tag == 2:
            tag = "historical site"
            result = get_attractions_for_traveler([name, location, [tag]])
            print(result)
            print("Goodbye :)")
            exit()
