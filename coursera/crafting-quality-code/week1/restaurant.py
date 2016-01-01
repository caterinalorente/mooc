'''
Created on Apr 8, 2013

@author: caterina

Write a function that has three parameters:
- a restaurant file that is open for reading.
- the price range ($, $$, $$$ and $$$$)
- a list of cuisines.

It returns a list of restaurants (in that price range serving at least one of those cuisines) 
and their ratings sorted from highest to lowest.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
'''

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'
      
def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)        
    
    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)    
    
    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)
    
    # We're done! Return that sorted list.
    return (result)
        
def read_restaurants(file):
    '''
        (file) -> (dict, dict, dict)
        
    Return a tuple of three dictionaries based on the information of the file:
     - a dict of {restaurant name: rating%}
     - a dict of {price: list of restaurant names}
     - a dict of {cuisine: list of restaurant names}
    '''
    
    name_to_rating = {}
    price_to_names = {'$':[], '$$':[], '$$$':[], '$$$$':[]}
    cuisine_to_names = {}
    
    content =  open(FILENAME, 'r').readlines()
    
    for i in range(0, len(content), 5):
        restaurant = content[i].strip('\n')
        rating = int(content[i+1].strip('\n')[:-1])
        price = content[i+2].strip('\n')
        cuisine = content[i+3].strip('\n')
        
        name_to_rating[restaurant] = rating
        price_to_names[price].append(restaurant)
        handle_cuisine_data(restaurant, cuisine, cuisine_to_names)
        
    return (name_to_rating, price_to_names, cuisine_to_names)

def handle_cuisine_data(restaurant, cuisine, cuisine_to_names):

    cuisine = cuisine.split(',')
    for item in cuisine:
        if item not in cuisine_to_names:
            cuisine_to_names[item] = []
        cuisine_to_names[item].append(restaurant)
        
    return cuisine_to_names

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    '''
    (list of str, dict of {str: list of str}, list of str) -> list of str
    
    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'],
                 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                 'Malaysian': ['Queen St. Cafe'],
                 'Thai': ['Queen St. Cafe'],
                 'Chinese': ['Dumplings R Us'],
                 'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    '''
    
    names_by_cuisine = []
    for name in names_matching_price:
        for cuisine in cuisines_list:
            for restaurant in cuisine_to_names[cuisine]:
                if restaurant == name:
                    names_by_cuisine.append(name)

def build_rating_list(name_to_rating, names_final):
    '''
    (dict of {str, int}, list of str) -> list of list [int, str]
    
    Return a list of [rating%, restaurant name], sorted by rating %            

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82, 
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
     
     >>> names = ['Queen St. Cafe', 'Dumplings R Us']
     >>> build_rating_list(name_to_rating, names)
     >>> [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
     '''
    
    names_by_rating = []
    for name in names_final:
        names_by_rating.append([name_to_rating[name], name])
    
    names_by_rating = sorted(names_by_rating, key=lambda x: x[1])
    

    return(names_by_rating)

print recommend(FILENAME, '$', ['Chinese', 'Pub Food'])