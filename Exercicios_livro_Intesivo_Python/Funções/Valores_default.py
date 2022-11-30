def describe_pet(pet_name, animal_type):
    """Describe a pet"""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s is {pet_name.title()}")


if __name__ == '__main__':
    describe_pet("harry", "cat")
    describe_pet("chicken", "tufik")
    describe_pet("wolf", "frida")