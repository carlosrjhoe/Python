def get_formatted_name(first_name, last_name, age=""):
    """get formatted name"""
    person = {'first': first_name, 'last': last_name}
    
    if age:
        person['age'] = age
    
    return person


if __name__ == "__main__":
    carlos = get_formatted_name('carlos', 'roberto', age=37)
    mayara = get_formatted_name('mayara', 'ramos')
    print(carlos)
    print(mayara)