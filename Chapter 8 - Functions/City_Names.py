"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned."""

def city_country(city, country):
    formatted_sentence = f"{city.title()}, {country.title()}"
    return formatted_sentence

cebu = city_country('cebu city', 'philippines')
tokyo = city_country('tokyo', 'japan')
paris = city_country('paris', 'france')

print(cebu)
print(tokyo)
print(paris)