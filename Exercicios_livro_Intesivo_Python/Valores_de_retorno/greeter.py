def get_formatted_name(first_name, last_name):
    """Retorna um nome completo de modo elegante"""
    full_name = f"{first_name} {last_name}"

    return full_name


if __name__ == "__main__":
    while True:
        print("\nPlease tell me your name:")
        print("(Enter 'Q' at any time to quit)")
        
        f_name = input("Your first name: ").title()
        if f_name == "Q":
            break
        
        l_name = input("Your last name: ").title()
        if l_name == "Q":
            break

        formatted_name = get_formatted_name(f_name, l_name)
        print(f"\nHello, {formatted_name}")