# city_functions.py
"""A collection of functions for working with cities."""

# def city_country(city, country):
#     """Return a string like 'Santiago, Chile'."""
#     return f"{city.title()}, {country.title()}" 

# def city_country(city, country, population):
#     """Return a string like 'Santiago, Chile - population 5000000'."""
#     output_string = f"{city.title()}, {country.title()}"
#     output_string += f" -population {population}"
#     return output_string 

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string 
            