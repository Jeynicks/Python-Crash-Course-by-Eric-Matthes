def city_country(city, country, population= 5_000_000):
    format_country = city.title() + ", " + country.title() + " -" + str(population)
    return format_country