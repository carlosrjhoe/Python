def get_formatted_name(first_name, last_name):
    """get formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


if __name__ == "__main__":
    print(get_formatted_name("carlos", "conceição"))
    print(get_formatted_name("mayara", "ramos"))
    print(get_formatted_name("neto", "conceição"))
    print(get_formatted_name("luna", "ramos"))