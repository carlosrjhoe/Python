def get_formatted_name(first_name, last_name, medlle_name=""):
    """get formatted name"""
    if medlle_name:
        full_name = f"{first_name} {medlle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()


if __name__ == "__main__":
    print(get_formatted_name("carlos", "conceição"))
    print(get_formatted_name("mayara", "ramos", "cordeiro"))
    print(get_formatted_name("neto", "conceição"))
    print(get_formatted_name("luna", "ramos", "conceição"))