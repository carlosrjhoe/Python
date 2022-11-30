def describe_pet(animal_type, pet_name):
    """Describe a pet"""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s is {pet_name.title()}")


if __name__ == '__main__':
    describe_pet(animal_type="cat", pet_name="harry")
    describe_pet(animal_type="dog", pet_name="tufik")
    describe_pet(animal_type="dog", pet_name="frida")