"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact.
Print the name of each city and all of the information you have stored about it."""

cities = {
    'Tokyo': {
            'country': 'Japan',
            'population': 37_000_000,
            'fact': 'It is the most populous metropolitan area in the world.'
    },
    
    'Cairo':{
            'country': 'Egypt',
            'population': 22_000_000,
            'fact': 'It is home to the famous Pyramids of Giza, one of the Seven Wonders of the Ancient World.'     
    },
    
    'Paris':{
            'country': 'France',
            'population': 11_000_000,
            'fact': 'Known as the “City of Light,” it is famous for the Eiffel Tower and its influence on art and culture.'
    },
    
    'New York City':{
            'country': 'United States',
            'population': 19_000_000,
            'fact': 'It is home to the United Nations Headquarters.'
    },
    
     'Rio de Janeiro':{
            'country': 'Brazil',
            'population': 6_700_000,
            'fact': 'Famous for its Christ the Redeemer statue and annual Carnival festival.'
    }
}

for city, infos in cities.items():
    print(f"{city} - \n"+
          f"Country: {infos['country']}\n"+
          f"Population: {infos['population']:,}\n"+
          f"Fact: {infos['fact']}\n")
    
