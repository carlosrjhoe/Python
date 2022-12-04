def city_country(city, country):
    city_country_format = f"{city.title()} - {country.title()}"
    return city_country_format


if __name__ == "__main__":
    print(f'{city_country("cabo de santo agostinho", "pernambuco")}')
    print(f'{city_country("recife", "pernambuco")}')
    print(f'{city_country("jaboatão", "pernambuco")}')
    print(f'{city_country("são paulo", "são paulo")}')
    print(f'{city_country("jardin são paulo", "são paulo")}')
    print(f'{city_country("rio de janeiro", "rio de janeiro")}')